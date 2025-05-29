import os
import subprocess
import uuid
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CodeSubmissionForm
from django.conf import settings
from problems.models import Problem

BASE_DIR = settings.BASE_DIR

def run_code(language, code, custom_input, code_id):
    # Determine file path for code
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
            compile_proc = subprocess.run(
                ['javac', code_file], capture_output=True, text=True
            )
            if compile_proc.returncode != 0:
                with open(output_file, 'w') as f:
                    f.write("Compilation Error:\n" + compile_proc.stderr)
                with open(output_file, 'r') as f:
                    return f.read()

            # Run Java
            code_dir = os.path.dirname(code_file) or '.'
            cmd = ['java', '-cp', code_dir, 'Main']

        else:
            return "Unsupported language"

        # Execute code with input redirection
        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            subprocess.run(
                cmd, stdin=infile, stdout=outfile,
                stderr=outfile, timeout=5
            )

    except subprocess.TimeoutExpired:
        with open(output_file, 'w') as f:
            f.write("Time Limit Exceeded")
    except subprocess.CalledProcessError as e:
        with open(output_file, 'w') as f:
            f.write(f"Compilation Error:\n{e}")
    except Exception as e:
        with open(output_file, 'w') as f:
            f.write(f"Error: {str(e)}")

    # Read and return output
    with open(output_file, 'r') as f:
        return f.read()


def compile_view(request):
    if request.method == 'POST':
        form = CodeSubmissionForm(request.POST)
        if form.is_valid():
            language = form.cleaned_data['language']
            code = form.cleaned_data['code']
            custom_input = form.cleaned_data['stdin']
            code_id = str(uuid.uuid4())

            ext_map = {
                'python': 'py',
                'cpp': 'cpp',
                'java': 'java',
                'c': 'c',
            }

            output = run_code(ext_map[language], code, custom_input, code_id)
            return render(request, 'output.html', {'output': output})
    else:
        form = CodeSubmissionForm()

    return render(request, 'compile_form.html', {'form': form})


def submit_code(request, problem_id):
    problem = get_object_or_404(Problem, pk=problem_id)
    action = request.POST.get('action')  # "run" or "submit"

    if request.method == 'POST':
        form = CodeSubmissionForm(request.POST)
        if form.is_valid():
            lang = form.cleaned_data['language']
            code = form.cleaned_data['code']
            stdin = form.cleaned_data['stdin']
            ext_map = {'py':'py','cpp':'cpp','c':'c','java':'java'}
            ext = ext_map[lang]
            code_id = str(uuid.uuid4())

            if action == 'run':
                output = run_code(ext, code, stdin, code_id)
                context = {
                    'output': output,
                    'problem_id': problem_id,
                    'was_run_only': True,
                }
                return render(request, 'output.html', context)

            elif action == 'submit':
                testcases = problem.testcases.all()
                results = []
                passed = 0
                for tc in testcases:
                    out = run_code(ext, code, tc.input_data, code_id)
                    ok = out.strip() == tc.expected_output.strip()
                    results.append({'input': tc.input_data,
                                    'expected': tc.expected_output,
                                    'output': out,
                                    'passed': ok})
                    if ok: passed += 1
                context = {
                    'results': results,
                    'total': len(testcases),
                    'passed': passed,
                }
                return render(request, 'submission_results.html', context)

    else:
        form = CodeSubmissionForm()

    return render(request, 'problem_detail.html', {'problem': problem, 'form': form})