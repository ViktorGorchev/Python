import math

try:
    paper_area = float(input())
    if paper_area <= 0.0:
        print('INVALID INPUT')

    box_height = float(input())
    box_width = float(input())
    box_length = float(input())
    if box_height <= 0.0 or box_width <= 0.0 or box_length <= 0.0:
        print('INVALID INPUT')

    paper_lost = (paper_area / 100.0) * 9.8
    box_area = 2 * (box_length * box_width) + 2 * (box_length * box_height) + 2 * (box_width * box_height)

    paper_needed = box_area / (paper_area - paper_lost)

    if math.floor(paper_needed) < paper_needed:
        paper_needed = math.floor(paper_needed) + 1
    print(paper_needed)

except:
    print('INVALID INPUT')