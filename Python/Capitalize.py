def solve(s):
    cap_name = []
    for name in s.split(" "):
        if name != "":
          if not name[0].isdigit():
              if len(name) > 1:
                cap_name.append(name[0].upper() + name[1:])
              else:
                cap_name.append(name[0].upper())
          else:
              cap_name.append(name)
        else:
            cap_name.append(name)
    return " ".join(cap_name)
        

if __name__ == '__main__':

    s = input()

    result = solve(s)

    print(result)
