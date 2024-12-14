# anki

# for what use
Place to create and manage Snyk related Anki material for onboarding, study, knowledge refresh, etc

# Getting Started (Update)
- Download Anki (link)
- Create Account? (This syncs your own progress)
- Import this package (.apkg)
- Add disabled policy to any decks you don't want to study?

# What is the organization ?
Decks to be organized under SnykCollab - meaning:
- in Anki they show up as SnykCollab::SubDeck
- In git they show up as SnykCollab-Subdeck.txt

# Why keep them in one big file?
- You can import everything at once, these are in the base folder
- This method can be noisy, really only recommended for "SnykCollab" - as it should cover most basic Snyk concepts
- I think SnykCollab will be the only one that is in a big file
- I would recommend importing decks from SnykAdvanced and SnykAdjacent one at a time, only when interested in the topic
	- I think keeping these monofiles updated is a PITA at this time and we shouldn't do it

# Why not keep them in one big file?
- I think there would be a lot of Git merge conflicts to remediate?  
- Also, people can more easily only import into Anki the decks they are interested in.  For example, there might be an easy, medium, advanced deck as people onboard?  Maybe you only want to import the easy deck?

# Why keep them in separate files?
- I'm finding this more useful the more I add additional, and sometimes crazier decks.  I really only want to import the subjects I care about otherwise it gets very noisy

# How to update?
- Update note(s)
- Export txt file with all options selected
- create new branch (git branch -c update-name)
- git push origin branchname

# What is the folder structure?
- top level
	- these keep things in separate decks completely:
		- SnykCollab: Basic information around Snyk, products, and related tech, ie, things you should know
		- SnykAdvanced: Advanced information around Snyk, products, and related tech - ie. things you CAN deep dive into
		- SnykAdjacent: Advanced info around other technology you may want to know for your job at Snyk (or outside) - things you can deep dive into if you really want to
	- each has a folder for individual decks below it
