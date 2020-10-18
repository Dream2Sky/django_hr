gender_female = 0
gender_male = 1
gender_other = 2

gender_choices = (
    (gender_female, "女"),
    (gender_male, "男"),
    (gender_other, "其他")
)

id_type_cn = 0
id_type_hk = 1
id_type_passport = 2

id_type_choices = (
    (id_type_cn, "身份证"),
    (id_type_hk, "港澳台身份证"),
    (id_type_passport, "外国护照"),
)

position_type_master = 0
position_type_parttime = 1
position_type_lend = 2
position_type_delegate = 3
position_type_help = 4
position_type_suspend = 5

position_type_choices = (
    (position_type_master, "主任职"),
    (position_type_parttime, "兼职"),
    (position_type_lend, "借调"),
    (position_type_delegate, "委派"),
    (position_type_help, "助勤"),
    (position_type_suspend, "挂职"),
)

position_status_onjob = 0
position_status_try = 1
position_status_quit = 2
position_status_choices = (
    (position_status_onjob, "在职"),
    (position_status_try, "试用"),
    (position_status_quit, "离职"),
)

entry_status_not_employed = 0
entry_status_employed = 1
entry_status_choices = (
    (entry_status_not_employed, "未入职"),
    (entry_status_employed, "已入职")
)
