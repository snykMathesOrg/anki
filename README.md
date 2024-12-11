# anki

# for what use
Place to create and manage Snyk related Anki material for onboarding, study, knowledge refresh, etc

# Getting Started (Update)
Download Anki (link)
Create Account? (This syncs your own progress)
Import this package (.apkg)
Add disabled policy to any decks you don't want to study?

# What is the organization ?
Decks to be organized under SnykCollab - meaning:
- in Anki they show up as SnykCollab::SubDeck
- In git they show up as SnykCollab-Subdeck.txt

# Why keep them in one big file?
Anki has a method for updating internally from apkg format, maybe better just to use apkg format?

# Why not keep them in one big file?
I think there would be a lot of Git merge conflicts to remediate?  
Also, people can more easily only import into Anki the decks they are interested in.  For example, there might be an easy, medium, advanced deck as people onboard?  Maybe you only want to import the easy deck?

# How to update?
Update note(s)
Export apkg file
create new branch (git branch -c update-name)
git push origin branchname

# What is the folder structure?
Not sure yet:
Acronyms
Products
Etc?
