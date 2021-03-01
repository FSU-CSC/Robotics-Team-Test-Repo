
def main(infile, outfile):

    f = open(infile, 'r')
    n = int(f.readline())
    echo, valid, summary = read(f, n)
    f.close()
    
    o = open(outfile, 'w')
    write(o, n, echo, valid, summary)
    o.close()
    
def read(f, n):
    
    valid = 0

    summary = []
    echo = []

    for line in f:
        error = ''
        l = line.strip()
        item, quantity = l.split()
        item, quantity = int(item), int(quantity)

        if item <= n and item > 0 and quantity > 0:
            valid += 1
            summary.append([item, quantity])
        elif item > n or item <= 0:
            error = "invalid item number"
        else:
            error = "invalid quantity"

        echo.append("%5d %10d %s" % (item, quantity, error))

    return echo, valid, summary

    
def write(o, n, echo, valid, summary):

    for i in echo:
        o.write(i + '\n')

    o.write("%10s\n" % '')
    o.write("Number of Valid Orders = %10d" % valid)
    o.write("\n%10s\n" % '')
    o.write("Summary:\n")
    summary.sort()

    summary = sort_summary(summary)
    while len(summary) > n:
        summary = sort_summary(summary)
    
    for i in range(0, len(summary)):
        o.write("%5d %10d\n" %(summary[i][0], summary[i][1]))
       
    return


def sort_summary(summary):
    for j in range(0,len(summary)):
        if j+1 < len(summary):
            if summary[j][0] == summary[j+1][0]:
                summary[j][1] += summary[j+1][1]
                summary.remove(summary[j+1])
        if j-1 >= 0 and j < len(summary):
            if summary[j-1][0] == summary[j][0]:
                summary[j-1][1] += summary[j][1]
                summary.remove(summary[j])
    return summary

    
