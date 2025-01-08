import anki

from anki.collection import Collection

wholeCollection = Collection(f"/Users/mathes/Library/Application Support/Anki2/User 1/collection.anki2")

#print(col.sched.deck_due_tree())

#snykCollab = col.decks.by_name("SnykCollab")
snykCollabId = wholeCollection.decks.id_for_name("SnykCollab")

#wholeCollection.export_anki_package()

wholeCollection.export_card_csv(out_path="test.csv", limit=0, with_html=True)