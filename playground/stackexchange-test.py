import stackexchange

search_term = "git reset"
so = stackexchange.Site(stackexchange.StackOverflow)

question = so.question(2530060)

print(question.title)
try:
    print(question.body)
except:
    pass

for answer in question.answers:
    print(answer)
    print()

# search_results = so.search(intitle=search_term)
