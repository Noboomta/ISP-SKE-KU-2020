# Commands for Remotes

Write the answers to these usage situations.

1. The command to list all your remote repositories, with their URL.
```
	git remote -v
```

2. The command to view details about a rempote repo named origin, including all the remote branches, and local tracking branches.
```
	git remote show origin
```

3. Suppose your remote repository (Github or `origin`) has a branch named `beverages` that you don't have in your local repository.  What is the command to create a new local branch as a copy of the remote `beverages` branch that **tracks** the remote branch?
    There are many commands that do this.  For your own reference you may want to write several.
```
	git checkout --track origin/beverages
	#or with these two commands
	git fetch
	git checkout beverages
```

4. Consider this situation:
   - you have a local repository including a README.md file.
   - Your local repo is up-to-date with a remote Github repo (has identical README.md)
   - You edit README.md on Github using Github's web interface and save the changes.
   - On your local machine, you edit README.md, commit the changes and push it to Github.    
   What happens when you push?    
   Explain why.
```
	your previous snapshot and last remote snapshot is not the same.
```

5. What are the steps to resolve the problem in the previous problem?
```
	git fetch
    git add -A
    git commit -m "message"
    git push
```

6. Suppose you want to move origin to a different URL. This can happen if you change the name of a repo on Github, or transfer ownership from one person to another. What is the command to change the URL for origin to https://github.com/your_name/newrepo.
```
	git remote set-url origin https://github.com/your_name/newrepo
```