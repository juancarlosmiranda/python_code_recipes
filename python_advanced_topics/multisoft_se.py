if __name__ == "__main__":
    print("main")
    s = ""
    a = [3, 8, 5, 1, 8, 5, 3, 2, 7]
    i = 0
    while i < len(a):
        print("---------------------------------")
        print(f"i={i} a[i]={a[i]}  a[i] % 2 != 0 {a[i] % 2 != 0} a[i]={a[i]} + a[a[i]]={a[a[i]]}")
        if a[i] % 2 != 0:
            print("yes ->")
            s += str(a[i] + a[a[i]])
            i += 2
            print(f"s={s} i={i}")
        else:
            print("NO ->")
            i -= 1
            print(f"s={s} i={i}")

    print("https://www.multisoft.se/" + s)
