import os
import subprocess
import uuid
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CodeSubmissionForm
from django.conf import settings
from problems.models import Problem

BASE_DIR = settings.BASE_DIR

def run_code(language, code, custom_input, code_id):
    if language == 'java':
        code_file = os.path.join(BASE_DIR, 'codes', 'Main.java')
    else:
        code_file = os.path.join(BASE_DIR, 'codes', f'{code_id}.{language}')
    input_file = os.path.join(BASE_DIR, 'inputs', f'{code_id}.txt')
    output_file = os.path.join(BASE_DIR, 'outputs', f'{code_id}.txt')

    # Ensure directories exist
    os.makedirs(os.path.dirname(code_file), exist_ok=True)
    os.makedirs(os.path.dirname(input_file), exist_ok=True)
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Save code and input
    with open(code_file, 'w') as f:
        f.write(code)
    with open(input_file, 'w') as f:
        f.write(custom_input or "")

    try:
        # Prepare command based on language
        if language == 'py':
            cmd = ['python3', code_file]
        elif language == 'cpp':
            exe_file = code_file.replace('.cpp', '')
            subprocess.run(['g++', code_file, '-o', exe_file], check=True)
            cmd = [exe_file]
        elif language == 'c':
            exe_file = code_file.replace('.c', '')
            subprocess.run(['gcc', code_file, '-o', exe_file], check=True)
            cmd = [exe_file]
        elif language == 'java':
        # Compile Java
            compile_proc = subprocess.run(['javac', code_file], capture_output=True, text=True)

            if compile_proc.returncode != 0:
                # Compilation failed — return stderr
                with open(output_file, 'w') as f:
                    f.write("Compilation Error:\n" + compile_proc.stderr)
                with open(output_file, 'r') as f:
                    return f.read()

            # Run Java
            code_dir = os.path.dirname(code_file) or '.'
            class_name = os.path.splitext(os.path.basename(code_file))[0]
            cmd = ['java', '-cp', code_dir, class_name]
        else:
            return "Unsupported language"

        # Execute code
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            subprocess.run(cmd, stdin=infile, stdout=outfile, stderr=outfile, timeout=5)

    except subprocess.TimeoutExpired:
        with open(output_file, 'w') as f:
            f.write("Time Limit Exceeded")
    except subprocess.CalledProcessError as e:
        with open(output_file, 'w') as f:
            f.write(f"Compilation Error:\n{e}")
    except Exception as e:
        with open(output_file, 'w') as f:
            f.write(f"Error: {str(e)}")

    # Read output
    with open(output_file, 'r') as f:
        output = f.read()

    return output


def compile_view(request):
    if request.method == 'POST':
        form = CodeSubmissionForm(request.POST)
        if form.is_valid():
            language = form.cleaned_data['language']
            code = form.cleaned_data['code']
            custom_input = form.cleaned_data['custom_input']
            code_id = str(uuid.uuid4())

            # Mapping for file extensions
            ext_map = {
                'python': 'py',
                'cpp': 'cpp',
                'java': 'java',  # Java not handled yet, just placeholder
                'c': 'c'
            }

            output = run_code(ext_map[language], code, custom_input, code_id)
            return render(request, 'output.html', {'output': output})
    else:
        form = CodeSubmissionForm()

    return render(request, 'compile_form.html', {'form': form})


def submit_code(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)

    if request.method == 'POST':
        form = CodeSubmissionForm(request.POST)
        if form.is_valid():
            # 1) pull form values
            language_key = form.cleaned_data['language']   # 'cpp', 'py', ...
            code             = form.cleaned_data['code']
            stdin            = form.cleaned_data['stdin']

            # 2) map to extension
            ext_map = {
                'py':  'py',
                'cpp': 'cpp',
                'c':   'c',
                'java': 'java'
            }
            ext = ext_map[language_key]

            # 3) generate a unique id for file names
            code_id = str(uuid.uuid4())

            # 4) actually compile & run
            output = run_code(ext, code, stdin, code_id)

            # 5) render the template
            return render(request, 'output.html', {
                'output': output,
                'problem': problem,
                'problem_id': problem_id,
            })
    else:
        form = CodeSubmissionForm()

    return render(request, 'problem_detail.html', {
        'problem': problem,
        'form': form,
    })