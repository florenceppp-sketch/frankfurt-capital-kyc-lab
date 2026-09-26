"""Run the teaching examples using only the Python standard library.

This checker is provided so you can focus on your assigned function.
Usage: python3 check_examples.py [fields|status|all]
"""

import argparse
from copy import deepcopy

from application_fields import missing_required_fields
from document_status import document_status_message
from examples import FIELD_EXAMPLES, STATUS_EXAMPLES


def check_group(label, function, examples):
    print("\n" + label)
    passed = 0
    for description, sample, expected in examples:
        argument = deepcopy(sample)
        try:
            actual = function(argument)
        except NotImplementedError:
            print("  TODO: " + description + " (implement your function first)")
        except Exception as error:
            print("  ERROR: " + description)
            print("    " + type(error).__name__ + ": " + str(error))
        else:
            if actual == expected and argument == sample:
                print("  PASS: " + description)
                passed += 1
            else:
                print("  FAIL: " + description)
                print("    Expected:", repr(expected))
                print("    Actual:  ", repr(actual))
                if argument != sample:
                    print("    The input was modified. Leave the input unchanged.")
    return passed, len(examples)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("task", nargs="?", choices=["fields", "status", "all"], default="all")
    task = parser.parse_args().task
    groups = []
    if task in ("fields", "all"):
        groups.append(("APPLICATION FIELDS", missing_required_fields, FIELD_EXAMPLES))
    if task in ("status", "all"):
        groups.append(("DOCUMENT STATUS", document_status_message, STATUS_EXAMPLES))

    passed = total = 0
    for group in groups:
        group_passed, group_total = check_group(*group)
        passed += group_passed
        total += group_total

    print("\nResult: " + str(passed) + "/" + str(total) + " examples passed.")
    return 0 if passed == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
