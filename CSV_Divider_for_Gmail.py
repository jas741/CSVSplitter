import pandas


df = pandas.read_csv("./MailingList.csv")


numbers = list(range(0,int(df.shape[0]/450)+2))
ranges = [x * 450 for x in numbers]
final = list(range(1,int(df.shape[0]/450)+2))

for n in final:
    df[int(ranges[n-1]):int(ranges[n])].to_csv("./MailingListNumber_" + str(n) + "_of_" + str(int(df.shape[0]/450)+1) + ".csv")




