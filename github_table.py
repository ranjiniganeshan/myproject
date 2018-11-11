from github import Github
from prettytable import PrettyTable

# or using an access token
g = Github(base_url="https://github.wdf.sap.corp/api/v3", login_or_token="160c8200bfc9f1ad33ea977a57dec99d429d635a")
org = input("Enter the name of the Organisation: ")
c = PrettyTable()


c.field_names = ["Org Name", "Repo Name", "Wikis", "Issues", "Projects", "Merge Commits", "Rebase merging","Branch Name", "Protection", "checks", "Reviews", "stale_reviews" ]


#for repo in g.get_user().get_repos():
for repo in g.get_organization(org).get_repos():
	print(repo.name)
	if not (repo.has_wiki and repo.has_issues and repo.has_projects and repo.allow_merge_commit and repo.allow_rebase_merge):
		print("Feautures are not set for this repo")
	else:
		print("Feautes are set please remove those")
	# repo1 = org.get_repos(repo.name)
	for team in repo.get_teams():
		print(team.name)
		if team.name in ['myteam','myteam111']:
			print("Cobalt team is added to repo")
		else:
			print("Cobalt team is not added to repo,please add")
		for branch in repo.get_branches():
			if not branch.name.startswith('CBLT'):
				print(repo.name)
				print("\t", branch.name)
				b = repo.get_branch(branch.name)
				if b.protected:
					print("Repo is --> ",repo.name, "| Branch --> ", b.name, " (protected)")
					x=b.get_required_status_checks()
					print(x.strict)
					y=b.get_required_pull_request_reviews()
					print(y.require_code_owner_reviews)
					print(y.dismiss_stale_reviews)
					if x.strict and y.require_code_owner_reviews and y.dismiss_stale_reviews:
					   print("This branch is as per the guidelines")

c.add_row([ org, repo.name, repo.has_wiki, repo.has_issues, repo.has_projects, repo.allow_merge_commit, repo.allow_rebase_merge,branch.name, b.protected, x.strict, y.require_code_owner_reviews, y.dismiss_stale_reviews ])
print(c)
