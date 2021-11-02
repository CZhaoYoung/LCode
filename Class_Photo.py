def classPhotos(red, blue):
    red.sort(reverse=True)
    blue.sort(reverse=True)

    shirtColorInFirstRow = "RED" if red[0] < blue[0] else "BLUE"

    for idx in range(len(red)):
        if shirtColorInFirstRow == "RED":
            if red[idx] >= blue[idx]:
                return False
        else:
            if blue <= red:
                return False

    return True


if __name__ == '__main__':
    red = [5,8,1,3,4]
    blue = [6,9,2,4,5]
    print(classPhotos(red, blue))