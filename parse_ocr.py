import xml.etree.ElementTree as ET
import re
import json
import numpy as np

text2 = """
    <html:html xmlns:html=\"http://www.w3.org/1999/xhtml\" lang=\"en\" xml:lang=\"en\">\n <html:head>\n  <html:title />\n<html:meta content=\"text/html;charset=utf-8\" http-equiv=\"Content-Type\" />\n  <html:meta content=\"tesseract 4.0.0-beta.4-50-g07acc\" name=\"ocr-system\" />\n  <html:meta content=\"ocr_page ocr_carea ocr_par ocr_line ocrx_word\" name=\"ocr-capabilities\" />\n</html:head>\n<html:body>\n  <html:div class=\"ocr_page\" id=\"page_1\" rotation=\"0\" title=\"image &quot;/home/vcap/tmp/9a706c10-06f1-4f23-91f0-c89d98c292220/pdfexample-8-81.png&quot;; bbox 0 0 3300 2550; ppageno 0\">\n   <html:div class=\"ocr_carea\" id=\"block_1_1\" title=\"bbox 1536 120 1775 140\">\n    <html:p class=\"ocr_par\" id=\"par_1_1\" lang=\"eng_best\" title=\"bbox 1536 120 1775 140\">\n     <html:span class=\"ocr_line\" id=\"line_1_1\" title=\"bbox 1536 120 1775 140; baseline 0 0; x_size 27.333334; x_descenders 6.8333335; x_ascenders 6.8333335\">\n      <html:span class=\"ocrx_word\" id=\"word_1_1\" title=\"bbox 1536 120 1775 140; x_wconf 95\"><html:strong><html:em>UNCLASSIFIED</html:em></html:strong></html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_2\" title=\"bbox 1276 195 3132 372\">\n    <html:p class=\"ocr_par\" id=\"par_1_2\" lang=\"eng_best\" title=\"bbox 1276 195 3132 372\">\n     <html:span class=\"ocr_line\" id=\"line_1_2\" title=\"bbox 1436 195 1855 223; baseline 0.002 -7; x_size 29; x_descenders 7; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_2\" title=\"bbox 1436 196 1634 223; x_wconf 95\"><html:strong><html:em>Department</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_3\" title=\"bbox 1657 195 1695 217; x_wconf 96\"><html:strong><html:em>of</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_4\" title=\"bbox 1716 195 1855 217; x_wconf 95\"><html:strong><html:em>Defense</html:em></html:strong></html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_3\" title=\"bbox 1396 231 1914 260; baseline 0 -7; x_size 28; x_descenders 6; x_ascenders 7\">\n      <html:span class=\"ocrx_word\" id=\"word_1_5\" title=\"bbox 1396 233 1436 253; x_wconf 96\"><html:strong><html:em>FY</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_6\" title=\"bbox 1458 231 1534 253; x_wconf 95\"><html:strong><html:em>2019</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_7\" title=\"bbox 1556 232 1774 254; x_wconf 94\"><html:strong><html:em>President's</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_8\" title=\"bbox 1796 232 1914 260; x_wconf 96\"><html:strong><html:em>Budget</html:em></html:strong></html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_4\" title=\"bbox 1276 269 2034 298; baseline 0 -7; x_size 29; x_descenders 7; x_ascenders 7\">\n      <html:span class=\"ocrx_word\" id=\"word_1_9\" title=\"bbox 1276 270 1414 291; x_wconf 93\"><html:strong><html:em>Exhibit</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_10\" title=\"bbox 1436 270 1493 291; x_wconf 77\"><html:strong><html:em>R-1</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_11\" title=\"bbox 1516 271 1556 291; x_wconf 96\"><html:strong><html:em>FY</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_12\" title=\"bbox 1578 269 1654 291; x_wconf 96\"><html:strong><html:em>2019</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_13\" title=\"bbox 1676 270 1894 292; x_wconf 90\"><html:strong><html:em>President's</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_14\" title=\"bbox 1916 270 2034 298; x_wconf 96\"><html:strong><html:em>Budget</html:em></html:strong></html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_5\" title=\"bbox 1377 308 3132 336; baseline 0.001 -7; x_size 28; x_descenders 7; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_15\" title=\"bbox 1377 308 1474 330; x_wconf 92\"><html:strong><html:em>Total</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_16\" title=\"bbox 1497 308 1734 336; x_wconf 91\"><html:strong><html:em>Obligational</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_17\" title=\"bbox 1755 308 1936 336; x_wconf 96\"><html:strong><html:em>Authority</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_18\" title=\"bbox 2977 310 3034 331; x_wconf 96\"><html:strong><html:em>Feb</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_19\" title=\"bbox 3059 309 3132 330; x_wconf 96\"><html:strong><html:em>2018</html:em></html:strong></html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_6\" title=\"bbox 1445 346 1868 372; baseline 0.002 -5; x_size 26; x_descenders 4; x_ascenders 7\">\n      <html:span class=\"ocrx_word\" id=\"word_1_20\" title=\"bbox 1445 346 1594 372; x_wconf 95\"><html:strong><html:em>(Dollars</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_21\" title=\"bbox 1618 346 1655 367; x_wconf 95\"><html:strong><html:em>in</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_22\" title=\"bbox 1677 346 1868 372; x_wconf 96\"><html:strong><html:em>Thousands)</html:em></html:strong></html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_3\" title=\"bbox 95 609 2013 1128\">\n    <html:p class=\"ocr_par\" id=\"par_1_3\" lang=\"eng_best\" title=\"bbox 1276 609 1974 631\">\n     <html:span class=\"ocr_line\" id=\"line_1_7\" title=\"bbox 1276 609 1974 631; baseline 0 0; x_size 28.666666; x_descenders 6.5; x_ascenders 6.6666665\">\n      <html:span class=\"ocrx_word\" id=\"word_1_23\" title=\"bbox 1276 611 1316 631; x_wconf 95\"><html:strong><html:em>FY</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_24\" title=\"bbox 1338 609 1414 631; x_wconf 95\"><html:strong><html:em>2019</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_25\" title=\"bbox 1556 611 1596 631; x_wconf 95\"><html:strong><html:em>FY</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_26\" title=\"bbox 1618 609 1694 631; x_wconf 95\"><html:strong><html:em>2019</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_27\" title=\"bbox 1836 611 1876 631; x_wconf 96\"><html:strong><html:em>FY</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_28\" title=\"bbox 1898 609 1974 631; x_wconf 96\"><html:strong><html:em>2019</html:em></html:strong></html:span>\n     </html:span>\n    </html:p>\n\n    <html:p class=\"ocr_par\" id=\"par_1_4\" lang=\"eng_best\" title=\"bbox 95 647 2013 1128\">\n     <html:span class=\"ocr_line\" id=\"line_1_8\" title=\"bbox 95 647 1956 679; baseline 0.001 -11; x_size 28.290321; x_descenders 6.2903223; x_ascenders 7\">\n      <html:span class=\"ocrx_word\" id=\"word_1_29\" title=\"bbox 95 647 355 678; x_wconf 95\"><html:strong><html:em>Appropriation</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_30\" title=\"bbox 1316 649 1396 679; x_wconf 96\"><html:strong><html:em>Base</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_31\" title=\"bbox 1596 649 1656 679; x_wconf 81\"><html:strong><html:em>oco</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_32\" title=\"bbox 1856 648 1956 679; x_wconf 95\"><html:strong><html:em>Total</html:em></html:strong></html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_9\" title=\"bbox 97 724 2013 750; baseline 0.001 -6; x_size 26; x_descenders 5; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_33\" title=\"bbox 97 724 267 748; x_wconf 96\"><html:strong><html:em>Research,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_34\" title=\"bbox 297 724 527 750; x_wconf 95\"><html:strong><html:em>Development,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_35\" title=\"bbox 558 725 633 745; x_wconf 93\"><html:strong><html:em>Test</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_36\" title=\"bbox 659 727 672 745; x_wconf 92\"><html:strong><html:em>&amp;</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_37\" title=\"bbox 696 724 787 749; x_wconf 95\"><html:strong><html:em>Eval,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_38\" title=\"bbox 816 725 894 750; x_wconf 94\"><html:strong><html:em>Army</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_39\" title=\"bbox 1259 724 1453 749; x_wconf 95\"><html:strong><html:em>10,159,379</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_40\" title=\"bbox 1598 724 1732 750; x_wconf 96\"><html:strong><html:em>325,104</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_41\" title=\"bbox 1819 724 2013 750; x_wconf 96\"><html:strong><html:em>10,484,483</html:em></html:strong></html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_10\" title=\"bbox 97 800 2012 826; baseline 0.001 -6; x_size 26; x_descenders 5; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_42\" title=\"bbox 97 800 267 824; x_wconf 95\"><html:strong><html:em>Research,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_43\" title=\"bbox 297 800 526 826; x_wconf 95\"><html:strong><html:em>Development,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_44\" title=\"bbox 557 801 632 821; x_wconf 93\"><html:strong><html:em>Test</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_45\" title=\"bbox 659 803 671 821; x_wconf 92\"><html:strong><html:em>&amp;</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_46\" title=\"bbox 696 800 786 825; x_wconf 95\"><html:strong><html:em>Eval,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_47\" title=\"bbox 816 801 894 826; x_wconf 95\"><html:strong><html:em>Navy</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_48\" title=\"bbox 1259 800 1453 826; x_wconf 95\"><html:strong><html:em>18,481,666</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_49\" title=\"bbox 1599 800 1732 826; x_wconf 96\"><html:strong><html:em>167,812</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_50\" title=\"bbox 1819 800 2012 826; x_wconf 95\"><html:strong><html:em>18,649,478</html:em></html:strong></html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_11\" title=\"bbox 97 875 2011 901; baseline 0.001 -6; x_size 26; x_descenders 5; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_51\" title=\"bbox 97 875 266 900; x_wconf 96\"><html:strong><html:em>Research,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_52\" title=\"bbox 296 875 526 901; x_wconf 94\"><html:strong><html:em>Development,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_53\" title=\"bbox 557 876 632 896; x_wconf 93\"><html:strong><html:em>Test</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_54\" title=\"bbox 659 878 671 896; x_wconf 92\"><html:strong><html:em>&amp;</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_55\" title=\"bbox 696 875 786 900; x_wconf 95\"><html:strong><html:em>Eval,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_56\" title=\"bbox 815 876 853 895; x_wconf 95\"><html:strong><html:em>AF</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_57\" title=\"bbox 1259 875 1452 901; x_wconf 96\"><html:strong><html:em>40,178,343</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_58\" title=\"bbox 1598 875 1731 901; x_wconf 94\"><html:strong><html:em>314,271</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_59\" title=\"bbox 1819 875 2011 901; x_wconf 95\"><html:strong><html:em>40,492,614</html:em></html:strong></html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_12\" title=\"bbox 97 951 2011 977; baseline 0.001 -6; x_size 26; x_descenders 5; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_60\" title=\"bbox 97 951 266 976; x_wconf 95\"><html:strong><html:em>Research,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_61\" title=\"bbox 296 951 526 977; x_wconf 95\"><html:strong><html:em>Development,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_62\" title=\"bbox 557 952 632 972; x_wconf 93\"><html:strong><html:em>Test</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_63\" title=\"bbox 659 954 671 972; x_wconf 92\"><html:strong><html:em>&amp;</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_64\" title=\"bbox 696 951 786 976; x_wconf 96\"><html:strong><html:em>Eval,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_65\" title=\"bbox 816 952 855 971; x_wconf 95\"><html:strong><html:em>DW</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_66\" title=\"bbox 1258 951 1452 977; x_wconf 95\"><html:strong><html:em>22,016,553</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_67\" title=\"bbox 1598 951 1731 977; x_wconf 95\"><html:strong><html:em>500,544</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_68\" title=\"bbox 1818 951 2011 977; x_wconf 96\"><html:strong><html:em>22,517,097</html:em></html:strong></html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_13\" title=\"bbox 97 1025 2012 1052; baseline 0.001 -6; x_size 26; x_descenders 5; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_69\" title=\"bbox 97 1025 312 1052; x_wconf 96\"><html:strong><html:em>Operational</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_70\" title=\"bbox 337 1027 412 1047; x_wconf 93\"><html:strong><html:em>Test</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_71\" title=\"bbox 439 1029 451 1047; x_wconf 93\"><html:strong><html:em>&amp;</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_72\" title=\"bbox 476 1026 566 1051; x_wconf 91\"><html:strong><html:em>Eval,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_73\" title=\"bbox 596 1026 733 1047; x_wconf 95\"><html:strong><html:em>Defense</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_74\" title=\"bbox 1318 1026 1452 1052; x_wconf 93\"><html:strong><html:em>221,009</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_75\" title=\"bbox 1878 1026 2012 1052; x_wconf 71\"><html:strong><html:em>221,009</html:em></html:strong></html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_14\" title=\"bbox 136 1100 2012 1128; baseline 0.001 -7; x_size 27; x_descenders 5; x_ascenders 7\">\n      <html:span class=\"ocrx_word\" id=\"word_1_76\" title=\"bbox 136 1100 233 1122; x_wconf 95\"><html:strong><html:em>Total</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_77\" title=\"bbox 255 1100 427 1126; x_wconf 96\"><html:strong><html:em>Research,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_78\" title=\"bbox 455 1100 687 1128; x_wconf 96\"><html:strong><html:em>Development,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_79\" title=\"bbox 716 1101 793 1122; x_wconf 93\"><html:strong><html:em>Test</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_80\" title=\"bbox 818 1102 832 1121; x_wconf 93\"><html:strong><html:em>&amp;</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_81\" title=\"bbox 855 1100 1054 1122; x_wconf 96\"><html:strong><html:em>Evaluation</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_82\" title=\"bbox 1259 1100 1387 1127; x_wconf 91\"><html:strong><html:em>91,056,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_83\" title=\"bbox 1399 1100 1452 1122; x_wconf 94\"><html:strong><html:em>950</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_84\" title=\"bbox 1558 1101 1732 1127; x_wconf 96\"><html:strong><html:em>1,307,731</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_85\" title=\"bbox 1819 1100 2012 1127; x_wconf 93\"><html:strong><html:em>92,364,681</html:em></html:strong></html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_4\" title=\"bbox 96 1213 2054 1242\">\n    <html:p class=\"ocr_par\" id=\"par_1_5\" lang=\"eng_best\" title=\"bbox 96 1213 2054 1242\">\n     <html:span class=\"ocr_line\" id=\"line_1_15\" title=\"bbox 96 1213 2054 1242; baseline 0.001 -8; x_size 28; x_descenders 7; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_86\" title=\"bbox 96 1213 194 1235; x_wconf 96\"><html:strong><html:em>Other</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_87\" title=\"bbox 215 1214 314 1234; x_wconf 95\"><html:strong><html:em>RDT&amp;E</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_88\" title=\"bbox 335 1213 453 1241; x_wconf 96\"><html:strong><html:em>Budget</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_89\" title=\"bbox 474 1213 673 1235; x_wconf 96\"><html:strong><html:em>Activities</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_90\" title=\"bbox 695 1214 753 1235; x_wconf 95\"><html:strong><html:em>Not</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_91\" title=\"bbox 778 1213 936 1235; x_wconf 96\"><html:strong><html:em>Included</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_92\" title=\"bbox 957 1213 994 1234; x_wconf 95\"><html:strong><html:em>in</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_93\" title=\"bbox 1016 1213 1074 1235; x_wconf 96\"><html:strong><html:em>the</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_94\" title=\"bbox 1095 1214 1267 1240; x_wconf 96\"><html:strong><html:em>Research,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_95\" title=\"bbox 1295 1214 1527 1242; x_wconf 95\"><html:strong><html:em>Development,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_96\" title=\"bbox 1556 1215 1633 1236; x_wconf 96\"><html:strong><html:em>Test</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_97\" title=\"bbox 1656 1214 1716 1236; x_wconf 96\"><html:strong><html:em>and</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_98\" title=\"bbox 1735 1214 1934 1236; x_wconf 96\"><html:strong><html:em>Evaluation</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_99\" title=\"bbox 1956 1214 2054 1236; x_wconf 95\"><html:strong><html:em>Title</html:em></html:strong></html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_5\" title=\"bbox 96 1290 2011 1468\">\n    <html:p class=\"ocr_par\" id=\"par_1_6\" lang=\"eng_best\" title=\"bbox 96 1290 2011 1468\">\n     <html:span class=\"ocr_line\" id=\"line_1_16\" title=\"bbox 97 1290 2011 1317; baseline 0.001 -6; x_size 27; x_descenders 5; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_100\" title=\"bbox 97 1290 213 1312; x_wconf 96\"><html:strong><html:em>Office</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_101\" title=\"bbox 237 1291 273 1312; x_wconf 95\"><html:strong><html:em>of</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_102\" title=\"bbox 296 1291 353 1312; x_wconf 96\"><html:strong><html:em>the</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_103\" title=\"bbox 379 1292 553 1317; x_wconf 95\"><html:strong><html:em>Inspector</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_104\" title=\"bbox 577 1291 712 1312; x_wconf 95\"><html:strong><html:em>General</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_105\" title=\"bbox 1359 1291 1451 1317; x_wconf 95\"><html:strong><html:em>1,602</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_106\" title=\"bbox 1919 1291 2011 1317; x_wconf 95\"><html:strong><html:em>1,602</html:em></html:strong></html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_17\" title=\"bbox 96 1365 2011 1392; baseline 0.001 -6; x_size 26; x_descenders 5; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_107\" title=\"bbox 96 1365 233 1387; x_wconf 95\"><html:strong><html:em>Defense</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_108\" title=\"bbox 257 1366 374 1387; x_wconf 95\"><html:strong><html:em>Health</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_109\" title=\"bbox 396 1367 535 1392; x_wconf 96\"><html:strong><html:em>Program</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_110\" title=\"bbox 1319 1366 1386 1392; x_wconf 95\"><html:strong><html:em>710,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_111\" title=\"bbox 1400 1366 1451 1387; x_wconf 96\"><html:strong><html:em>637</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_112\" title=\"bbox 1879 1366 2011 1392; x_wconf 95\"><html:strong><html:em>710,637</html:em></html:strong></html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_18\" title=\"bbox 97 1441 2011 1468; baseline 0.001 -6; x_size 27; x_descenders 5; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_113\" title=\"bbox 97 1441 175 1463; x_wconf 96\"><html:strong><html:em>Chem</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_114\" title=\"bbox 195 1442 312 1468; x_wconf 91\"><html:strong><html:em>Agents</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_115\" title=\"bbox 339 1445 351 1463; x_wconf 93\"><html:strong><html:em>&amp;</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_116\" title=\"bbox 375 1441 552 1463; x_wconf 96\"><html:strong><html:em>Munitions</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_117\" title=\"bbox 576 1441 793 1463; x_wconf 96\"><html:strong><html:em>Destruction</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_118\" title=\"bbox 1319 1442 1451 1468; x_wconf 94\"><html:strong><html:em>886,728</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_119\" title=\"bbox 1879 1442 2011 1468; x_wconf 95\"><html:strong><html:em>886,728</html:em></html:strong></html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_6\" title=\"bbox 96 1515 675 1538\">\n    <html:p class=\"ocr_par\" id=\"par_1_7\" lang=\"eng_best\" title=\"bbox 96 1515 675 1538\">\n     <html:span class=\"ocr_line\" id=\"line_1_19\" title=\"bbox 96 1515 675 1538; baseline 0.002 -1; x_size 27.32258; x_descenders 5.3225803; x_ascenders 7\">\n      <html:span class=\"ocrx_word\" id=\"word_1_120\" title=\"bbox 96 1515 252 1538; x_wconf 96\"><html:strong><html:em>National</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_121\" title=\"bbox 276 1517 413 1538; x_wconf 95\"><html:strong><html:em>Defense</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_122\" title=\"bbox 438 1516 572 1538; x_wconf 94\"><html:strong><html:em>Sealift</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_123\" title=\"bbox 596 1517 675 1538; x_wconf 94\"><html:strong><html:em>Fund</html:em></html:strong></html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_7\" title=\"bbox 136 1591 2012 1619\">\n    <html:p class=\"ocr_par\" id=\"par_1_8\" lang=\"eng_best\" title=\"bbox 136 1591 2012 1619\">\n     <html:span class=\"ocr_line\" id=\"line_1_20\" title=\"bbox 136 1591 2012 1619; baseline 0.001 -7; x_size 27; x_descenders 5; x_ascenders 6\">\n      <html:span class=\"ocrx_word\" id=\"word_1_124\" title=\"bbox 136 1591 233 1613; x_wconf 96\"><html:strong><html:em>Total</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_125\" title=\"bbox 255 1592 313 1613; x_wconf 96\"><html:strong><html:em>Not</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_126\" title=\"bbox 337 1591 374 1612; x_wconf 96\"><html:strong><html:em>in</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_127\" title=\"bbox 395 1591 567 1617; x_wconf 94\"><html:strong><html:em>Research,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_128\" title=\"bbox 595 1591 827 1619; x_wconf 95\"><html:strong><html:em>Development,</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_129\" title=\"bbox 856 1592 933 1613; x_wconf 93\"><html:strong><html:em>Test</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_130\" title=\"bbox 958 1593 972 1612; x_wconf 92\"><html:strong><html:em>&amp;</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_131\" title=\"bbox 995 1591 1194 1613; x_wconf 96\"><html:strong><html:em>Evaluation</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_132\" title=\"bbox 1278 1591 1452 1618; x_wconf 83\"><html:strong><html:em>1,598,967</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_133\" title=\"bbox 1838 1591 2012 1618; x_wconf 94\"><html:strong><html:em>1,598,967</html:em></html:strong></html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n   <html:div class=\"ocr_carea\" id=\"block_1_8\" title=\"bbox 1534 2389 3132 2443\">\n    <html:p class=\"ocr_par\" id=\"par_1_9\" lang=\"eng_best\" title=\"bbox 1534 2389 3132 2443\">\n     <html:span class=\"ocr_line\" id=\"line_1_21\" title=\"bbox 2975 2389 3132 2414; baseline 0.006 -6; x_size 37.25; x_descenders 6.5; x_ascenders 10.25\">\n      <html:span class=\"ocrx_word\" id=\"word_1_134\" title=\"bbox 2975 2389 3052 2414; x_wconf 96\"><html:strong><html:em>Page</html:em></html:strong></html:span>\n      <html:span class=\"ocrx_word\" id=\"word_1_135\" title=\"bbox 3078 2389 3132 2409; x_wconf 95\"><html:strong><html:em>IIB</html:em></html:strong></html:span>\n     </html:span>\n     <html:span class=\"ocr_line\" id=\"line_1_22\" title=\"bbox 1534 2423 1773 2443; baseline 0 0; x_size 37.25; x_descenders 6.5; x_ascenders 10.25\">\n      <html:span class=\"ocrx_word\" id=\"word_1_136\" title=\"bbox 1534 2423 1773 2443; x_wconf 93\"><html:strong><html:em>UNCLASSIFIED</html:em></html:strong></html:span>\n     </html:span>\n    </html:p>\n   </html:div>\n  </html:div>\n </html:body>\n</html:html>

"""

ns = {'html': "http://www.w3.org/1999/xhtml"}


def main():

    # text2_old = text2
    tree = ET.fromstring(text2)

    try:
        open('export_text.txt', 'w').close()
    except:
        print('Not made yet')
    f = open('export_text.txt', 'w')

    allText = []
    allTextObjects = []
    allTextObjectsByLine = []
    currentText = ''
    lineNum = 0

    # Loop through all nodes in the xml tree
    for node in tree.iter():
        word = False
        line = False
        if('class' in node.attrib):
            cl = getClass(node)
            if(cl == 'ocr_line'):
                line = True
            if(cl == 'ocrx_word'):
                word = True
            if(line):
                print(
                    '---------------NEW LINE----------------------------------------------------------------')
                f.write(
                    '---------------NEW LINE----------------------------------------------------------------' + '\n')
                allText.append(currentText)
                lineNum += 1

                currentText = ''
            if(line or word):
                print('node: \t\t\t' + str(node))
                f.write('node: \t\t\t\t' + str(node) + '\n')
                print('attrib: \t\t' + str(getAttrib(node)))
                f.write('attrib: \t\t\t' + str(getAttrib(node)) + '\n')
                print('attrib[\'class\']: \t' + str(getClass(node)))
                f.write('attrib[\'class\']: \t' +
                        str(getClass(node)) + '\n')
                print('attrib[\'title\']: \t' + str(getTitle(node)))
                f.write('attrib[\'title\']: \t' +
                        str(getTitle(node)) + '\n')
                getBoundingBox(node)
            if(word):
                text = getText(node)
                # text = text_out.find("em", ns)
                print('text: \t\t\t' + str(text))
                f.write('text: \t\t\t\t' + str(text) + '\n')
                currentText += ' ' + text
                textObject = {"text": getText(node),
                              "bbox": getBoundingBox(node)}
                allTextObjects.append(textObject)
            print()
            f.write('\n')
    allText.append(currentText)

    for i in allText:
        print(i)
    print("Left, Top, Right, Bottom")
    for i in allTextObjects:
        print(i)

    # Get columns
    rightJustified = getUniqueValues(allTextObjects, 2)
    rightMatches = getSimilarValues(rightJustified, 3, 1)
    topJustified = getUniqueValues(allTextObjects, 1)
    topMatches = getSimilarValues(topJustified, 5, 0)
    # print(rightJustified)
    print()
    # print(rightMatches)
    # print(topMatches)
    # print(topMatches.keys())
    # print(len(rightMatches.keys()))
    # print(len(topMatches.keys()))
    # print(lineNum)
    # for i in rightJustified.values():
    #     print(len(i))

    # for key, value in rightMatches.items():
    #     a = np.array(value)
    #     rightMatches[key] = a.ravel()
    # for key, value in rightMatches.items():
    #     print(key)
    #     print(len(value))
    #     print(value)
    #     print()
    # for key, value in rightJustified.items():
    #     print(key)
    #     print(value)
    #     print()
    for key, value in rightMatches.items():
        print(key)
        print(value)
        print()


def getUniqueValues(allTextObjects, boxIndex):
    justified = {}
    for i in allTextObjects:
        if i['bbox'][boxIndex] not in justified:
            justified[i['bbox'][int(boxIndex)]] = [i]
        else:
            justified[i['bbox'][boxIndex]].append(i)
    for key, value in justified.items():
        a = np.array(value)
        justified[key] = a.ravel()
    return justified


def getSimilarValues(justified, distance, sortIndex):
    found = []
    match = {}
    for i in justified.keys():
        if i in found:
            continue
        else:
            match[i] = [justified[i]]
            for j in justified.keys():
                if(i == j) or (j in found):
                    continue
                else:
                    if(abs(int(i) - int(j)) < distance):
                        found.append(j)
                        match[i].append(justified[j])
    for key, value in match.items():
        match[key] = np.concatenate(value).ravel().tolist()
        # match[key] = match[key].sort(key=lambda x: x['bbox'][sortIndex])
    return match

# arrange all words by line
# check for overallap if... last word in line, or word to right of line is far (not part of same sentence)


def getBoundingBox(node):
    return re.findall(r'\d+', getTitle(node))


def getText(node):
    if('class' in getAttrib(node)):
        if(getClass(node) == 'ocrx_word'):
            for child in node.iter():
                if(child.tag.endswith("em")):
                    print(child.text)
                    return child.text


def getClass(node):
    return getAttrib(node)['class']


def getTitle(node):
    return getAttrib(node)['title']


def getAttrib(node):
    return node.attrib


def getDistance(bbox1, bbox2, direction):
    if(direction == 'TB'):
        return abs(int(bbox1[1]) - int(bbox2[3]))
    if(direction == 'BT'):
        return abs(int(bbox1[3]) - int(bbox2[1]))
    if(direction == 'LR'):
        return abs(int(bbox1[0]) - int(bbox2[2]))
    if(direction == 'RL'):
        return abs(int(bbox1[2]) - int(bbox2[0]))
    if(direction == 'LL'):
        return abs(int(bbox1[0]) - int(bbox2[0]))
    if(direction == 'RR'):
        return abs(int(bbox1[2]) - int(bbox2[2]))


if __name__ == "__main__":
    main()