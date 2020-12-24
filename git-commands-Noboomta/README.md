[Git Basic](#part-1-basics)
[Adding and Changing Stuff](#part-2-adding-and-changing-stuff)
[Undoing Changes](#part-3-undoing-changes)
[Branch and Merge](#part-4-branch-and-merge)
[Remote Commands](remote-commands.md)
## Part 1. Basics

1. When working with Git locally, what are these?  Describe each one in a sentence

   **Staging area** - area between  the  git directory and the local working directory.
   **Working copy** - copy of the recently work.
   **master** - main branch to working that created after use ```git init```.
   **HEAD** - the pointer of the current branch that you're using

2. A git commit includes the author's name and email.  How does git know your name and email?  When you install git on a new machine (or in a new user account) you should perform what 2 git commands?
    ```
    Git configuration commands for a new account
    git config --global user.name "Puvana Swatvanith"
	git config --global user.email puvana.s@example.com

    ```
3. There are 2 ways to create a local Git repository.  What are they?
    - create  new repository by using git init
    - clone a repository to your local by using git clone <url>


4. Suppose you create a git repository in a directory (folder) named "/project1". Where does git put the repository files for this project? Write the path to git's files.
    - for Linux: /home/user/project1
	- for macOS: /Users/user/project1
	- for Windows: C:/Users/user/project1

### Part 2. Adding and Changing Stuff

Suppose your working copy of a repository contains these files and directories:
```
README
out/
     a.exe
src/ a
     b
	 c
test/
     d
```     

1. What is the command to add README and *everything* in the `src` directory to the git staging area?

```
	git add README out/
```

2. Write the command to add `test/d` to the staging area.

```
	git add test/
```

3. Write a command to list files in the staging area.

```
	git status
```

4. You decide you **don't** want to add `test/d` to git.  Write the command to remove `test/d` from the staging area.

'''
    git -rm `test/d`
'''

5. Write the command to commit the staging area to the repository.

```
	git commit -m <commit message>
```

6. You **never** want any files in the `out/` directory to be commited to git. Describe 2 steps to configure git for this:
	* echo 'out/' >  .gitignore
	* git add .gitignore; git commit -m "Add .gitignore to ignore any files in 'out/'"


7. What is the command to move `a`, `b`, and `c` from the `src` directory to the top-level directory of the project, so that they are also moved in the git repository?

```
	git add a b c
	git commit -m "moved src directory"
```

8. Commit this change with the message "moved src directory".

```
	mv src/* .
```

9. If you change a **lot** of files, using `git add` for each one can be tedious.  Write a command to add *all modified files* to the staging area.   
    (After doing this you should use "git status" to verify you didn't add unintended files.)
```
	git add -A
```

10. What is the command to delete the file `c` from both your working copy **and** the repository? (This stages the change but it is not deleted from repo until you commit it.)
```
	git rm c
```

11. What is the command to show all differences between your working copy and the most recent commit? (Can be kind of hard to read.)

% git diff oldCommit newCommit

## Part 3. Undoing Changes

1. Use an editor to make some changes to file `a`.  What is the command to view the **differences** between your working copy `a` and the current version in repository?
```
	git diff a
```

2. You decide you don't like the changes to `a`. What is the command to **replace** your working copy of `a` with the current version in the repository?    
    (This also works if you accidentally *delete* a file from your working copy.)
```
	git reset
```

3. How do you "undo" a commit?  What is the command to move the "head" of the current branch to the **previous** commit?

```
	git reset HEAD^
```

## Part 4. Branch and Merge

1. What is the command to create a new branch named `dev-food`?
```
	git branch dev-food
```

2. What is the command to print what your current branch is?

```
	git branch --show-current
```

3. What command to list **all** branches including remote ones?

```
	git branch --all
```

4. What is command to switch your working copy to a branch named `dev-food`?

```
	git checkout dev-food
```

5. You commit some files to `dev-food` and try to "push" them to Github, but it fails:

    ```
    cmd>  git checkout dev-food
    cmd>  git push
    fatal:  The current branch dev-food has no upstream branch. 
    ```
    Explain this error.

6. What is the command to push `dev-food` to `origin` as a new remote branch on `origin`?

    ```
	you don't have a branch dev-food so you have to push the branch to the reposity by using 'git push -u origin dev-food'.
```

7. Suppose your remote repository (Github or `origin`) has a branch named `beverages` that you don't have in your local repository.  What is the command to create a new local branch as a copy of the remote `beverages` branch that **tracks** the remote branch?
    There are many commands that do this.  For your own reference you may want to write several.
```
	git checkout --track origin/beverages
	#or with these two commands
	git fetch
	git checkout beverages
```

8. Consider this situation:
   - you have a local repository including a README.md file.
   - Your local repo is up-to-date with a remote Github repo (has identical README.md)
   - You edit README.md on Github using Github's web interface and save the changes.
   - On your local machine, you edit README.md, commit the changes and push it to Github.    
   What happens when you push?    
   Explain why.
```
	your previous snapshot and last remote snapshot is not the same.
```

## Viewing Changes and Commits

* Command to show the history of a repository in the terminal (command) window.  This form shows one line per commit, with a graph, and all branches.
    ```
    git log --oneline --graph --all
    ```
    Some versions of git have an *alias* "log1" for this (`git log1`).

* The GUI tool `gitk` or `gitk --all` displays even more info about the commit history.


* The output of `git diff` can be hard to read. To view differences more visually:

    1. View differences on Github.
    2. Meld or Diffuse to compare and merge files. `git difftool` lists more tools.
    3. `gitk` shows diffs between commits
    4. Eclipse EGit shows side-by-side diffs and can merge interactively

---
## Resources

[Learn Git Interactive Tutorial][LearnGitInteractive] excellent visual tutorial.   
[Git Visualizer][VisualizeGit] execute Git commands and see the results as a graph.    
[Pro Git Online Book][ProGit]    
[Pro Git PDF][ProGitPdf] free download

[ProGit]: https://www.git-scm.com/book/en/v2 "Pro Git online book on Git-scm.com"
[ProGitPdf]: https://progit2.s3.amazonaws.com/en/2016-03-22-f3531/progit-en.1084.pdf "Pro Git v.2 PDF on AWS. Longer, book format."
[LearnGitInteractive]: https://learngitbranching.js.org "Interactive graphical git tutorial"
[VisualizeGit]: http://git-school.github.io/visualizing-git/ "Online tools draws a graph of commits in a repo, as you type"
