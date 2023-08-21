states = ("Alabama, Alaska, Arizona, Arkansas, California, Colorado, Connecticut, Delaware, Florida")
list_states = states.split(", ")

list_states.append("Wyoming")

list_states[4] = "Kalifornia"

list_states.extend(["idaho", "oregon"])

print(list_states)
