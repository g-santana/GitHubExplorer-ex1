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

token = 'fe56f6d0724beb94a756fb59079d5f637b5fd858'
headers = {"Authorization": "Bearer " + token}

# query example {
#   search(query:"stars:>100", first:10, type:REPOSITORY){
#     pageInfo{
#       hasNextPage
#       endCursor
#     }
#     edges{
#       node{
#         ... on Repository{
#           name
#           createdAt
#           pullRequests(states:MERGED){
#             totalCount
#           }
#           releases{
#             totalCount
#           }
#           updatedAt
#           primaryLanguage {
#             name
#           }
#           closedIssues:issues(states:CLOSED){
#             totalCount
#           }
#           totalIssues:issues{
#             totalCount
#           }
#         }
#       }
#     }
#   }
# }

    # query example{
    # 	search(query:"stars:>100", type:REPOSITORY, first:10){
    # 		pageInfo{
    # 		    hasNextPage
    # 		    endCursor
    # 		}
    #         nodes{
    #             ...on Repository{
    #                 name
    #                 createdAt
    #                 pullRequests(states:MERGED){
    #                     totalCount
    #                 }
    #                 releases{
    #                     totalCount
    #                 }
    #                 updatedAt
    #                 primaryLanguage {
    #                     name
    #                 }
    #                 closedIssues:issues(states:CLOSED){
    #                     totalCount
    #                 }
    #                 totalIssues:issues{
    #                     totalCount
    #                 }
    #             }
    #         }
    #     }
    # }