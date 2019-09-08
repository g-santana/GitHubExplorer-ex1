query = """
query example{
	search(query:"stars:>100", type:REPOSITORY, first:100){
		pageInfo{
		    hasNextPage
		    endCursor
		}
		nodes{
			...on Repository{
                nameWithOwner
		    }
	    }
    }
}
"""

token = '' # insert token here
headers = {"Authorization": "Bearer " + token}
