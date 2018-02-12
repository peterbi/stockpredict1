def main():
    gitig = open(".gitignore", "a")
    with open(".gitrid") as conf:
        for(mc, linec) in enumerate(conf):
            filename,start,end = linec.split(" ")
            gitig.write(filename+"\n")
            start = int(start)
            end = int(end)
            outfilename = "GR" + filename
            outfile = open(outfilename, "w+")
            with open(filename) as infile:
                for(n, line) in enumerate(infile):
                    if (n+1<start or n+1>end):
                        outfile.write(str(line))
                    else:
                        outfile.write("#redacted\n")



main()
