# Test_Commit_Revert

A simple exercise for practicing ( Test && Commit || Revert )
This is an activity for TC3405 course.

## Prepare environment

- Using VsCode install [Run on Save](https://marketplace.visualstudio.com/items?itemName=emeraldwalk.RunOnSave)
- Go to settings: 
  - File > Preferences > Settings 
  - hitting Ctrl + , (Cmd + , if you’re on a Mac).  
- In the left side menu click on `Extensions`
- Look for the extension `Run On Save` (Reload vscode if it doesn't appear)
- Open settings.json
- Inside emeraldwalk.runonsave add: 
``` json
    "commands": [
            {
                "match": "(.+\\\\Test_Commit_Revert\\\\tests_stringcalculator\\.py|.+\\/Test_Commit_Revert\\/tests_stringcalculator\\.py)",
                "cmd": "git add ./tests_stringcalculator.py && git commit -m \"test\""
            },
            {
                "match": "(.+\\\\Test_Commit_Revert\\\\stringcalculator\\.py|.+\\/Test_Commit_Revert\\/stringcalculator\\.py)",
                "cmd": "python ./tests_stringcalculator.py && git commit -am progress || git reset --hard",
                "runIn": "terminal"
            },
        ]
```
- Your file should have the structure as the settings.json in this repository


## Instructions

- Fork this repository into your Github.
- Perform the following TCR challenge before the talk about this topic.
 
### String Calculator Kata (via Roy Osherove)

- Create a simple String calculator with a method int Add(string numbers). The method can take 0, 1 or 2 numbers, and will return their sum (for an empty string it will return 0). For example "" or "1" or "1,2"
  - Start with the simplest test case of an empty string and move to 1 and two numbers.
  - Remember to solve things as simple as possible so that you force yourself to write tests you did not think about.
  - Remember to refactor after each passing test.
- Allow the Add method to handle an unknown amount of numbers.
- Allow the Add method to handle new lines between numbers (instead of commas).
  - the following input is ok: "1\n2,3" (will equal 6)
  - the following input is NOT ok: "1,\n" (not need to prove it - just clarifying)
- Support different delimiters. To change a delimiter, the beginning of the string will contain a separate line that looks like this: [delimiter]\n[numbers...], for example ;\n1;2 should return three where the default delimiter is ; .
  - The first line is optional. all existing scenarios should still be supported
- Calling Add with a negative number will throw an exception "negatives not allowed" - and the negative that was passed. 
  - if there are multiple negatives, show all of them in the exception message

## Notes

- Every time you save `stringcalculator.py` it will run the tests, if they fail then your changes in the file will be reverted
- To see the output of the test if they don't appear in terminal, go to `Output` (it's next to terminal, you can open it directly with ctrl+shit+u) and select `Run On Save` from the selection box
- Every time you save `tests_stringcalculator.py` it will save that change without a problem.