# i made this into a story make it more fun to read hehe


#  You arrive at a wildly popular restaurant. The host is guarding a
# reservation ledger (dataset.txt). Your friends keep asking:
# "Is my name on the list? is it is it????" (queries.txt)
#
# Your job is to answer in order, writing "YES" if the name is on the reservation
# list and "NO" if it’s not. No arguing with the host; the ledger is law.
#


def load_lines(path):
    
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return {line.strip() for line in f if line.strip()}

def dataset_search(dataset_path, queries_path, out_path):
   
    reservations = load_lines(dataset_path)

    
    with open(out_path, "w", encoding="utf-8") as out, open(queries_path, "r", encoding="utf-8") as qf:
        for raw in qf:
            name = raw.strip()
            if not name:
                continue  
            out.write(("YES" if name in reservations else "NO") + "\n")

if __name__ == "__main__":
    print("Host stand is open. Checking reservations...")
    dataset_search("dataset.txt", "queries.txt", "resurvations_are_you_in.txt")
    print("All guests checked. See results.txt for who’s getting a table.")


