import language_check

f1 = open('out.txt', 'r')
text = f1.read()
f1.close()
tool = language_check.LanguageTool('en-US')
matches = tool.check(text)
f2 = open('final.txt', 'w+')
f2.write(language_check.correct(text, matches))
f2.close()
