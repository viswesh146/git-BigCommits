"""
**Functionality:**

This module is useful for three purpose:

    1) You want to find the big commits happened in your git repo and who has
       committed that at what time.

    2) You want to find the dormant branches in your git repo and who is the
       author of the branch

    3) You want to prevent large commits in your local repo.

*NOTE:* All you need to do is give your repositry location as input to this
module. It does not need your git credentials.
Also, It will find large commits across all branches present in the repo

Supported Outputs:

    1) Reports can be generated as HTML file.
    2) Console output

Usage:

You can run the main function of git_html_report to generate the html output

Once you install this package, two commands will be available to you.

bigcommits - it will print the fat files in your repo to the console.
bigcommits-html - it will generate the html report of fat files in your repo.





"""
