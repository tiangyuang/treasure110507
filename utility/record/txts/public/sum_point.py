from utility import DB

# //總點數
def sum_point(line_id):
    sum_point = DB.run(("select sum(b.Sub_Get_points) from treasure_recycling_record as a join treasure_sub_record as b on a.Record_Recycling_number=b.Sub_Recycling_number where a.Record_LINEid='%s'" %(line_id)),'2')[0]
    
    return str(sum_point)