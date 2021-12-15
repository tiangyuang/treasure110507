import DB
line_id = 'U0131826f2d23e1f17a3689d8574fd2cb'
sum_point = DB.run(("select sum(b.Sub_Get_points) from treasure_recycling_record as a join treasure_sub_record as b on a.Record_Recycling_number=b.Sub_Recycling_number where a.Record_LINEid='%s'" %(line_id)),'2')[0]
print(str(round(sum_point,2)))