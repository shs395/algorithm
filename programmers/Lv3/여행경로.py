answer = []

def dfs(node, arr, ticket_len, ticket_dict, visited_dict):
    global answer
    temp = arr[:]
    temp.append(node)
    if len(temp) == ticket_len + 1:
        answer = temp
        return True
    if node in ticket_dict:
        for next_node in ticket_dict[node]:
            if visited_dict[node + next_node] > 0:
                visited_dict[node + next_node] -= 1
                if dfs(next_node, temp, ticket_len, ticket_dict, visited_dict) == False:
                    visited_dict[node + next_node] += 1
    return False
        
def solution(tickets):
    tickets.sort(key=lambda x:x[1])
    ticket_dict = dict()
    visited_dict = dict()
    for ticket in tickets:
        if ticket[0] in ticket_dict:
            ticket_dict[ticket[0]].append(ticket[1])
        else:
            ticket_dict[ticket[0]] = [ticket[1]]
        
        if ticket[0] + ticket[1] in visited_dict:
            visited_dict[ticket[0] + ticket[1]] += 1
        else:
            visited_dict[ticket[0] + ticket[1]] = 1

    dfs('ICN', [], len(tickets), ticket_dict, visited_dict)
    return answer
# solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
# solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
# solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]])
# solution([["ICN", "SFO"], ["SFO", "ICN"], ["ICN", "SFO"], ["SFO", "QRE"]])
solution([["ICN", "A"], ["ICN", "B"], ["B", "ICN"]])