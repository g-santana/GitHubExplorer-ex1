query = """
query example{
    search(query:"stars:>100", type:REPOSITORY, first:10){
        repositoryCount
        nodes{
            ...on Repository{
                name
                createdAt
                updatedAt
                releases{
                    totalCount
                }
                primaryLanguage{
                    name
                }
                pullRequests(states: MERGED){
                    totalCount
                }
                closedIssues : issues(states: CLOSED){
                    totalCount
                }
                totalIssues: issues{
                    totalCount
                }
            }
        }
        pageInfo{
            hasNextPage
            endCursor
        }
    }
}
"""

token = ''	# insert token here
headers = {"Authorization": "Bearer " + token}

