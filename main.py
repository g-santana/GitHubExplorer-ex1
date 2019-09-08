import myfuncs
import json
import pandas

if __name__ == '__main__':
    ans = myfuncs.get_all_repos()
    # for i in ans:
    #     print(i)
    ans = json.dumps(ans)
    ans = json.loads(ans)
    # print(ans)
    pandas.read_json(ans.to_csv('repodata.csv'))
    with open('repodata.csv') as f:
        print(f.read())
