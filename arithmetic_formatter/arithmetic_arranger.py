import operator

MAX_PROBLEMS = 5
MAX_DIGITS_PER_OPERAND = 4
PROBLEM_SPACER = " " * 4  # Space between two problems
OP_FILLER = 2  # Substitution for operator + whitespace

ops = {"+": operator.add, "-": operator.sub}


def arithmetic_arranger(problems, show_results=False):
    if __too_many_problems(problems):
        return "Error: Too many problems."

    problem_counter = 0
    line1 = ""
    line2 = ""
    dashes = ""
    result_line = ""

    for problem in problems:
        problem_counter += 1
        expressions = problem.split()

        num1 = expressions[0]
        op = expressions[1]
        num2 = expressions[2]

        if __exceed_digit_limit(num1, num2):
            return "Error: Numbers cannot be more than four digits."
        if not __are_digits(num1, num2):
            return "Error: Numbers must only contain digits."
        if not __is_correct_operator(op):
            return "Error: Operator must be '+' or '-'."

        result = __calculate_result(num1, op, num2)

        problem_width = __get_larger_operand(num1, num2)

        line1 += num1.rjust(OP_FILLER + problem_width)
        line2 += op + " " + num2.rjust(problem_width)
        dashes += "-" * (OP_FILLER + problem_width)
        result_line += result.rjust(OP_FILLER + problem_width)

        if not __is_last_problem(problem_counter, problems):
            line1 += PROBLEM_SPACER
            line2 += PROBLEM_SPACER
            dashes += PROBLEM_SPACER
            result_line += PROBLEM_SPACER

    arranged_problems = line1 + "\n" + line2 + "\n" + dashes

    if show_results:
        arranged_problems += "\n" + result_line

    return arranged_problems


def __too_many_problems(problems):
    return len(problems) > MAX_PROBLEMS


def __is_correct_operator(op):
    return op == '+' or op == '-'


def __exceed_digit_limit(num1, num2):
    return len(num1) > MAX_DIGITS_PER_OPERAND or len(
        num2) > MAX_DIGITS_PER_OPERAND


def __are_digits(num1, num2):
    return num1.isdigit() and num2.isdigit()


def __calculate_result(num1, op, num2):
    result = ops[op](int(num1), int(num2))
    return str(result)


def __is_last_problem(problem_counter, problems):
    return problem_counter == len(problems)


def __get_larger_operand(num1, num2):
    return max(len(num1), len(num2))
