import myfuncs
import json
import csv


def write_data_to_json():
    ans = myfuncs.get_all_repos()
    # print(len(ans))
    repos = []
    for cell in ans:
        repos.append(cell)
    with open("repo_data.json", "w") as f:
        json.dump(repos, f, indent=4)


def from_json_to_csv():
    with open("repo_data.json", "r") as f:
        repos = json.load(f)
    # print(json.dumps(repos, indent=4))
    output = open("repo_data.csv", "w")
    out_csv = csv.writer(output)
    out_csv.writerow(repos[0].keys())
    for row in repos:
        out_csv.writerow(row.values())


if __name__ == '__main__':
    # write_data_to_json()  # ideia: executar poucas vezes, para nao estourar o limite de requisicoes
    from_json_to_csv()      # ideia: usar o json aqui salvo das requisicoes para escrever o csv

