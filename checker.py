import language_check
import sys

tool = language_check.LanguageTool('en-US')
text = sys.argv[1]
matches = tool.check(text)
if len(matches) > 0:
    print()
    print("********************** POSSIBLE ERRORS ****************************")
    for i in range(len(matches)):
        print(matches[i])
else:
    print()
    print("********************** NO ERRORS DETECTED *************************")
