.. GitBigCommits documentation master file, created by
   sphinx-quickstart on Tue Jan 30 19:00:03 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to GitBigCommits's documentation!
=========================================

**Installation**

   Even if you are new to python, it is fairly easy to execute this and get
   your report.

   To run this, you need two things.

   1) `Python <https://www.python.org/downloads/>`_.
   2) `Pip <https://pip.pypa.io/en/stable/installing/#do-i-need-to-install
   -pip>`_ (Package Manger for Python).

Python is by default installed if you are using Linux or MAC, so
all you need to do is install Pip.

For MAC:

   .. code-block:: bash

        sudo easy_install pip

For Linux, detailed article is `here <https://www.tecmint.com/install-pip-in-linux/>`_

Once you have installed, you can run the below to get this up and running.

      .. code-block:: bash

          pip install Gitbigcommits


This is compatible with both Python2 and Python3.

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

  ``pip install Gitbigcommits``

Once you install, the following below commands will be available to you in your
 terminal.

 1) bigcommits - prints big commits to stdout
 2) bigcommits-html - creates a html file and writes the report to that.
 3) dbranch-html - find the dormant branch in your repo and writes into a html
 4) bigcommits-prevent - once you execute this, your local repo will prevent
    large commits to be happened in your repo

**Supported Outputs:**

    1) Reports can be generated as HTML file.
    2) Console output

**Usage:**

bigcommits <git_location_in_your_machine> <size_in_kb>

*Eg:*

            .. code-block:: bash

              $bigcommits "usr/home/myrepo/" 1024

Your git directory is in the "usr/home/myrepo" folder. git directory denotes
where your ".git" folder is present.

Similarly,

  .. code-block:: bash

   $bigcommits-html "usr/home/myrepo/" 1024

   $dbranch-html "usr/home/myrepo/" 1

   $bigcommits-prevent "usr/home/myrepo/"

if you are a developer, looking for more reports or customization, directly
look into :ref:`git-core-label`. docs

Sample initialization

   .. code-block:: python

      >>>from gitbigcommits.core.git_commit_utility import GitFatCheckutility
      >>>git_util = GitFatCheckutility('/usr/home/repo', '1024')
      >>>git_util.get_all_file_with_info()


.. automodule:: gitbigcommits

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   gitbigcommits
   gitbigcommits.core
   gitbigcommits.report_layer

