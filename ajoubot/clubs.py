# -*- coding: utf-8 -*-
import pymysql
import requests

conn = pymysql.connect(
        host="localhost",
        user = "root",
        passwd = "1q2w3e4r",
        db = "ajou",
        charset = "utf8",
        use_unicode=True
)

cur = conn.cursor()

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (1, '의과대학','SIX Lines','음악')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (2, '의과대학','탯줄','연극')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (3, '의과대학','CMF','종교')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (4, '의과대학','ㅎ.ㅁ 사랑','봉사')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (5, '의과대학','Medic Chamber','오케스트라')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (6, '의과대학','ARTISTS','미술')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (7, '의과대학','ORBIT','사진')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (8, '의과대학','메디콤','컴퓨터')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (9, '의과대학','아메바','농구')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (10, '의과대학','Papyrus','독서토론')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (11, '의과대학','꼼지락','사회과학')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (12, '의과대학','단','축구')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (13, '의과대학','CODON','분자생물학')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (14, '의과대학','아가페','종교')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (15, '간호대학','SIX Lines','음악')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (16, '간호대학','탯줄','연극')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (17, '간호대학','CMF','종교')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (18, '간호대학','ㅎ.ㅁ 사랑','봉사')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (19, '간호대학','Media Chamber','오케스트라')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (20, '간호대학','ARTISTS','미술')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (21, '간호대학','ORBIT','사진')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (22, '간호대학','메디콤','컴퓨터')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (23, '간호대학','S.O.S','수화')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (24, '간호대학','아메바','농구')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (25, '간호대학','Papyrus','독서토론')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (26, '간호대학','꼼지락','사회과학')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (27, '간호대학','단','축구')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (28, '간호대학','CODON','분자생물학')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (29, '간호대학','사랑나눔','봉사')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (30, '국제학부','국제통상연구회','소학회')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (31, '국제학부','일본연구회','소학회')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (32, '국제학부','중국연구회','소학회')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (33, '정보통신대학','HAMER','소학회','사이버보안학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (34, '정보통신대학','WHOIS','소학회','사이버보안학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (35, '정보통신대학','크리스탈','소학회','전자공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (36, '정보통신대학','새','사회과학','전자공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (37, '정보통신대학','오반칙','농구','전자공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (38, '정보통신대학','일레븐','축구','전자공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (39, '정보통신대학','하늘음표','음악','전자공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (40, '정보통신대학','COMP D&A','소학회','전자공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (41, '정보통신대학','네트로닉스','소학회','전자공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (42, '정보통신대학','ISB-AJOU','소학회','전자공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (43, '정보통신대학','ANSI','소학회','소프트웨어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (44, '정보통신대학','CC','소학회','소프트웨어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (45, '정보통신대학','HANTOR','소학회','소프트웨어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (46, '정보통신대학','SWARP','소학회','소프트웨어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (47, '정보통신대학','THIS','음악','소프트웨어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (48, '정보통신대학','PLATANUS','음악','소프트웨어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (49, '정보통신대학','ZOCCER','축구','소프트웨어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (50, '정보통신대학','DoiT!','소학회','소프트웨어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (51, '정보통신대학','CHAOS','농구','소프트웨어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (52, '정보통신대학','BALLAND','축구','소프트웨어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (53, '정보통신대학','TML','게임개발','소프트웨어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (54, '정보통신대학','KHRONIES','소학회','소프트웨어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (55, '정보통신대학','소리벗','음악','미디어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (56, '정보통신대학','브레인스톰','소학회','미디어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (57, '정보통신대학','발자국','사회과학','미디어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (58, '정보통신대학','잉크','만화','미디어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (59, '정보통신대학','F.C MEDIA','축구','미디어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (60, '정보통신대학','커넥트','소학회','미디어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (61, '정보통신대학','Souna','소학회','미디어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (62, '정보통신대학','아티젠','소학회','미디어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (63, '정보통신대학','고래','소학회','미디어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (64, '정보통신대학','FeelM','사진','미디어학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (65, '사회과학대학','몸부림','사회과학','경제학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (66, '사회과학대학','소리샘','토론','경제학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (67, '사회과학대학','zenith','공연','경제학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (68, '사회과학대학','씨알의 소리','공연','경제학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (69, '사회과학대학','C & N','토론','경제학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (70, '사회과학대학','자아죽달','소학회','경제학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (71, '사회과학대학','사커노믹스','축구','경제학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (72, '사회과학대학','셈틀','컴퓨터','행정학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (73, '사회과학대학','루카스','공연','행정학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (74, '사회과학대학','P.A.S.S','축구','행정학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (75, '사회과학대학','등줄기','토론','행정학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (76, '사회과학대학','낮에 나온 반달','봉사','심리학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (77, '사회과학대학','사람과 사회','소학회','심리학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (78, '사회과학대학','심씨네','영화','심리학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (79, '사회과학대학','안한숙밴드','공연','심리학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (80, '사회과학대학','이중자아','연극','심리학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (81, '사회과학대학','심볼','체육','심리학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (82, '사회과학대학','범인','소학회','심리학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (83, '사회과학대학','See Real','소학회','심리학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (84, '사회과학대학','반딧불이','토론','사회학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (85, '사회과학대학','올레','체육','사회학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (86, '사회과학대학','소름','영화','사회학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (87, '사회과학대학','민중사랑','소학회','정치외교학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (88, '사회과학대학','S.A.C.T','등산','정치외교학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (89, '사회과학대학','카리스마','축구','정치외교학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (90, '사회과학대학','아레테','공연','정치외교학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (91, '사회과학대학','SPOILER','소학회','스포츠레저학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (92, '경영대학','AFIA','소학회','경영학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (93, '경영대학','AAA','소학회','경영학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (94, '경영대학','New Venture','창업','경영학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (95, '경영대학','RPM','소학회','경영학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (96, '경영대학','CF','소학회','경영학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (97, '경영대학','모짤트','영어','경영학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (98, '경영대학','COSBI','소학회','경영학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (99, '경영대학','GAGE','토론','경영학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (100, '경영대학','AJOUNET','소학회','경영학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (101, '경영대학','증권연구회','소학회','경영학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (102, '경영대학','경영심리','소학회','경영학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (103, '경영대학','Global & Comparative Management','토론','경영학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (104, '경영대학','B-Cube','컴퓨터','e-비즈니스 학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (105, '경영대학','CORE','소학회','e-비즈니스 학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (106, '경영대학','ESC','축구','e-비즈니스 학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (107, '경영대학','DTI','소학회','e-비즈니스 학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (108, '경영대학','Vbiz','소학회','e-비즈니스 학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (109, '경영대학','FEBSi','컴퓨터','금융공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (110, '경영대학','AFLO','소학회','금융공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (111, '인문대학','나들목','발표','국어국문학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (112, '인문대학','바투','체육','국어국문학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (113, '인문대학','시숲','소학회','국어국문학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (114, '인문대학','해방말뚝','사물놀이','국어국문학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (115, '인문대학','길들이기','토론','영어영문학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (116, '인문대학','Over Spirit','연극','영어영문학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (117, '인문대학','줄리메','축구','영어영문학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (118, '인문대학','징검다리','공연','영어영문학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (119, '인문대학','날개','영화','영어영문학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (120, '인문대학','샘N샘','임용고시','영어영문학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (121, '인문대학','Les Amateurs','소학회','불어불문학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (122, '인문대학','Nouveauté','소학회','불어불문학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (123, '인문대학','더사리','소학회','불어불문학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (124, '인문대학','바우','음악','사학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (125, '인문대학','역사기행반','소학회','사학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (126, '인문대학','사나래','토론','사학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (127, '인문대학','세아','토론','사학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (128, '인문대학','시나리오 나무','소학회','문화컨텐츠학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (129, '인문대학','콘텐츠 오브 레전드','소학회','문화컨텐츠학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (130, '인문대학','463 야구단','야구','문화컨텐츠학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (131, '약학대학','藥, 오름','등산','문화컨텐츠학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (132, '약학대학','APC','사진','문화컨텐츠학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (133, '약학대학','구사모','농구','문화컨텐츠학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (134, '약학대학','맛동','소학회','문화컨텐츠학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (135, '약학대학','아뮤너스','봉사','문화컨텐츠학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (136, '약학대학','아벨','소학회','문화컨텐츠학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (137, '약학대학','아약스','축구','문화컨텐츠학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (138, '약학대학','야키스','야구','문화컨텐츠학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (139, '약학대학','전어','음악','문화컨텐츠학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (140, '약학대학','청춘책방','토론','문화컨텐츠학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (141, '약학대학','팝크루','춤','문화컨텐츠학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (142, '자연과학대학','MATHLAB','소학회','수학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (143, '자연과학대학','M&E','영어','수학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (144, '자연과학대학','파이','소학회','수학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (145, '자연과학대학','스톡킹','소학회','수학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (146, '자연과학대학','No-name','소학회','물리학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (147, '자연과학대학','No-STAR','소학회','물리학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (148, '자연과학대학','ALCHEMY','소학회','화학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (149, '자연과학대학','B.E.S.T','소학회','생명과학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (150, '자연과학대학','늑대야','공연','생명과학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (151, '자연과학대학','MOSS','공연')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (152, '자연과학대학','백두마루','사물놀이')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (153, '자연과학대학','전투체육','축구')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (154, '자연과학대학','반공해','소학회')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (155, '정보통신대학','소금꽃','문예창작')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (156, '정보통신대학','고슴도치','만화')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (157, '중앙동아리','아미','미술')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (158, '중앙동아리','A.SA','사진')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (159, '중앙동아리','묵우회','서예')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (160, '중앙동아리','씨네아리랑','영화')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (161, '중앙동아리','AD.BRAIN','광고')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (162, '중앙동아리','AJESS','영어')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (163, '중앙동아리','PLUS+','발표')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (164, '중앙동아리','TIME','영어')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (165, '중앙동아리','ANC','영어')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (166, '중앙동아리','시사문제강독회','시사')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (167, '중앙동아리','BUT','영상')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (168, '중앙동아리','C.OB.E','천문')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (169, '중앙동아리','DoiT!','컴퓨터')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (170, '중앙동아리','아미콤','컴퓨터')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (171, '중앙동아리','ATOM','로봇')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (172, '중앙동아리','유레카','발명')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (173, '중앙동아리','산악부','등산')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (174, '중앙동아리','A-pin','볼링')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (175, '중앙동아리','무한공간','패러글라이딩')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (176, '중앙동아리','돌벗','바둑')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (177, '중앙동아리','Drop-IN','스노우보드')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (178, '중앙동아리','ROA','자전거')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (179, '중앙동아리','차오름','태권도')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (180, '중앙동아리','호완','권투')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (181, '중앙동아리','아주도','유도')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (182, '중앙동아리','2.5G','탁구')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (183, '중앙동아리','ABC','농구')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (184, '중앙동아리','AFC','축구')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (185, '중앙동아리','ATC','테니스')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (186, '중앙동아리','ABBA','야구')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (187, '중앙동아리','아주도','검도')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (188, '중앙동아리','꽁','스쿼시')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (189, '중앙동아리','클리어','배드민턴')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (190, '중앙동아리','CMI','종교')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (191, '중앙동아리','CCC','종교')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (192, '중앙동아리','SFC','종교')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (193, '중앙동아리','아가생','봉사')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (194, '중앙동아리','호우회','봉사')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (195, '중앙동아리','호롱불','봉사')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (196, '중앙동아리','샘터야학','야학')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (197, '중앙동아리','카포','음악')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (198, '중앙동아리','PTP','봉사')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (199, '중앙동아리','이데알레','봉사')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (200, '중앙동아리','녹두벌','풍물')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (201, '중앙동아리','B.E.A.T','힙합')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (202, '중앙동아리','5분쉼표','실용음악')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (203, '중앙동아리','스파이더스','록')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (204, '중앙동아리','글리','합창')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (205, '중앙동아리','미디올로지','MIDI')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (206, '중앙동아리','아몽극회','연극')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (207, '중앙동아리','아르떼','기타')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (208, '중앙동아리','소울','흑인음악')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (209, '중앙동아리','맨차','축구')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (210, '중앙동아리','AJUDO','유도')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category) VALUES (211, '중앙동아리','사커노믹스','축구')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (212, '공과대학','노루막이','소학회','기계공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (213, '공과대학','A-FA','소학회','기계공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (214, '공과대학','List21','소학회','산업공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (215, '공과대학','ASECON','소학회','산업공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (216, '공과대학','M&S','소학회','산업공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (217, '공과대학','FC.Prime','소학회','산업공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (218, '공과대학','Archon','소학회','산업공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (219, '공과대학','알고사는사람들','독서토론','산업공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (220, '공과대학','UAV','소학회','산업공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (221, '공과대학','아금바리','경제','화학공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (222, '공과대학','터뷸런스','축구','화학공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (223, '공과대학','트로잔스','농구','화학공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (224, '공과대학','아람','소학회','신소재공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (225, '공과대학','FC FCC','축구','신소재공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (226, '공과대학','가치','소학회','신소재공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (227, '공과대학','소리바람','공연','응용화학생명공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (228, '공과대학','Back Tackle','축구','응용화학생명공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (229, '공과대학','아로마틱','공연','응용화학생명공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (230, '공과대학','BC플러랜','농구','응용화학생명공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (231, '공과대학','터 지기','소학회','환경안전공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (232, '공과대학','지구방위대','축구','환경안전공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (233, '공과대학','창건','소학회','건설시스템공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (234, '공과대학','미공','소학회','건설시스템공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (235, '공과대학','가람지기','소학회','건설시스템공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (236, '공과대학','아토스','농구','건설시스템공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (237, '공과대학','적토마','축구','건설시스템공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (238, '공과대학','Ats','소학회','교통시스템공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (239, '공과대학','ATFC','축구','교통시스템공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (240, '공과대학','TuF','소학회','교통시스템공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (241, '공과대학','Fly High','농구','교통시스템공학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (242, '공과대학','공간모음','소학회','건축학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (243, '공과대학','바로서기','소학회','건축학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (244, '공과대학','상상','소학회','건축학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (245, '공과대학','A2','축구','건축학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (246, '공과대학','A-bit','소학회','건축학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (247, '공과대학','AREA','소학회','건축학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (248, '공과대학','B2','농구','건축학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (249, '공과대학','CMRZ','소학회','건축학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (250, '공과대학','DP&E','사진','건축학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (251, '공과대학','DSA','소학회','건축학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (252, '공과대학','E-CUBIC','소학회','건축학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (253, '공과대학','FACE','소학회','건축학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (254, '공과대학','Studio I.S.M','소학회','건축학과')")

cur.execute("INSERT INTO club(idclub, club_univ, club_name, club_category, club_major) VALUES (255, '공과대학','UD2','소학회','건축학과')")

conn.commit()

conn.close()
