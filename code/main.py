import timetable_maker

timetable_maker = timetable_maker.Maker('../resources/cabinets.docx',
                              '../resources/plan.xlsx',
                              '../resources/class_quantity.docx')
timetable_maker.make()