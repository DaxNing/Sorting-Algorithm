# 排序算法
排序算法的详细比较

<html xmlns:o="urn:schemas-microsoft-com:office:office"
xmlns:x="urn:schemas-microsoft-com:office:excel"
xmlns="http://www.w3.org/TR/REC-html40">

<head>
<meta http-equiv=Content-Type content="text/html; charset=gb2312">
<meta name=ProgId content=Excel.Sheet>
<meta name=Generator content="Microsoft Excel 15">
<link rel=File-List href="排序算法时间复杂度1.files/filelist.xml">
<!--table
	{mso-displayed-decimal-separator:"\.";
	mso-displayed-thousand-separator:"\,";}
.font58237
	{color:windowtext;
	font-size:9.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:等线;
	mso-generic-font-family:auto;
	mso-font-charset:134;}
.font68237
	{color:black;
	font-size:11.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:等线;
	mso-generic-font-family:auto;
	mso-font-charset:134;}
.font78237
	{color:black;
	font-size:11.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:等线;
	mso-generic-font-family:auto;
	mso-font-charset:134;}
.font88237
	{color:black;
	font-size:11.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:等线;
	mso-generic-font-family:auto;
	mso-font-charset:134;}
.xl158237
	{padding-top:1px;
	padding-right:1px;
	padding-left:1px;
	mso-ignore:padding;
	color:black;
	font-size:11.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:等线;
	mso-generic-font-family:auto;
	mso-font-charset:134;
	mso-number-format:General;
	text-align:general;
	vertical-align:bottom;
	mso-background-source:auto;
	mso-pattern:auto;
	white-space:nowrap;}
.xl638237
	{padding-top:1px;
	padding-right:1px;
	padding-left:1px;
	mso-ignore:padding;
	color:black;
	font-size:11.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:等线;
	mso-generic-font-family:auto;
	mso-font-charset:134;
	mso-number-format:General;
	text-align:center;
	vertical-align:bottom;
	border:.5pt solid windowtext;
	mso-background-source:auto;
	mso-pattern:auto;
	white-space:nowrap;}
.xl648237
	{padding-top:1px;
	padding-right:1px;
	padding-left:1px;
	mso-ignore:padding;
	color:black;
	font-size:11.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:等线;
	mso-generic-font-family:auto;
	mso-font-charset:134;
	mso-number-format:General;
	text-align:general;
	vertical-align:bottom;
	border:.5pt solid windowtext;
	mso-background-source:auto;
	mso-pattern:auto;
	white-space:nowrap;}
.xl658237
	{padding-top:1px;
	padding-right:1px;
	padding-left:1px;
	mso-ignore:padding;
	color:black;
	font-size:11.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:等线;
	mso-generic-font-family:auto;
	mso-font-charset:134;
	mso-number-format:General;
	text-align:center;
	vertical-align:middle;
	border:.5pt solid windowtext;
	mso-background-source:auto;
	mso-pattern:auto;
	white-space:nowrap;}
.xl668237
	{padding-top:1px;
	padding-right:1px;
	padding-left:1px;
	mso-ignore:padding;
	color:black;
	font-size:11.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:等线;
	mso-generic-font-family:auto;
	mso-font-charset:134;
	mso-number-format:General;
	text-align:center;
	vertical-align:bottom;
	border:.5pt solid windowtext;
	mso-background-source:auto;
	mso-pattern:auto;
	white-space:nowrap;}
ruby
	{ruby-align:left;}
rt
	{color:windowtext;
	font-size:9.0pt;
	font-weight:400;
	font-style:normal;
	text-decoration:none;
	font-family:等线;
	mso-generic-font-family:auto;
	mso-font-charset:134;
	mso-char-type:none;}
-->
</head>

<body>
<!--[if !excel]>　　<![endif]-->
<!--下列信息由 Microsoft Excel 的发布为网页向导生成。-->
<!--如果同一条目从 Excel 中重新发布，则所有位于 DIV 标记之间的信息均将被替换。-->
<!----------------------------->
<!--“从 EXCEL 发布网页”向导开始-->
<!----------------------------->

<div id="排序算法时间复杂度_8237" align=center x:publishsource="Excel">

<table border=0 cellpadding=0 cellspacing=0 width=647 style='border-collapse:
 collapse;table-layout:fixed;width:487pt'>
 <col width=69 span=2 style='width:52pt'>
 <col width=107 style='mso-width-source:userset;mso-width-alt:3434;width:81pt'>
 <col width=109 style='mso-width-source:userset;mso-width-alt:3477;width:82pt'>
 <col width=125 style='mso-width-source:userset;mso-width-alt:3989;width:94pt'>
 <col width=99 style='mso-width-source:userset;mso-width-alt:3157;width:74pt'>
 <col width=69 style='width:52pt'>
 <tr height=19 style='height:14.0pt'>
  <td rowspan=2 height=38 class=xl638237 width=69 style='height:28.0pt;
  width:52pt'>类别</td>
  <td rowspan=2 class=xl638237 width=69 style='width:52pt'>排序方法</td>
  <td colspan=3 class=xl638237 width=341 style='border-left:none;width:257pt'>时间复杂度</td>
  <td rowspan=2 class=xl638237 width=99 style='width:74pt'>空间复杂度</td>
  <td rowspan=2 class=xl638237 width=69 style='width:52pt'>稳定性</td>
 </tr>
 <tr height=19 style='height:14.0pt'>
  <td height=19 class=xl638237 style='height:14.0pt;border-top:none;border-left:
  none'>最好</td>
  <td class=xl638237 style='border-top:none;border-left:none'>平均</td>
  <td class=xl638237 style='border-top:none;border-left:none'>最坏</td>
 </tr>
 <tr height=22 style='height:16.5pt'>
  <td rowspan=2 height=44 class=xl638237 style='height:33.0pt;border-top:none'>插入排序</td>
  <td class=xl648237 style='border-top:none;border-left:none'>直接插入</td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N)</td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N<font
  class="font78237"><sup>2</sup></font><font class="font68237">)</font></td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N<font
  class="font78237"><sup>2</sup></font><font class="font68237">)</font></td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(1)</td>
  <td class=xl658237 style='border-top:none;border-left:none'>稳定</td>
 </tr>
 <tr height=22 style='height:16.5pt'>
  <td height=22 class=xl648237 style='height:16.5pt;border-top:none;border-left:
  none'>希尔排序</td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N)</td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N<font
  class="font78237"><sup>1.3</sup></font><font class="font68237">)</font></td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N<font
  class="font78237"><sup>2</sup></font><font class="font68237">)</font></td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(1)</td>
  <td class=xl658237 style='border-top:none;border-left:none'>不稳定</td>
 </tr>
 <tr height=22 style='height:16.5pt'>
  <td rowspan=2 height=43 class=xl638237 style='height:32.5pt;border-top:none'>选择排序</td>
  <td class=xl648237 style='border-top:none;border-left:none'>直接选择</td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N)</td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N<font
  class="font78237"><sup>2</sup></font><font class="font68237">)</font></td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N<font
  class="font78237"><sup>2</sup></font><font class="font68237">)</font></td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(1)</td>
  <td class=xl658237 style='border-top:none;border-left:none'>不稳定</td>
 </tr>
 <tr height=21 style='height:16.0pt'>
  <td height=21 class=xl648237 style='height:16.0pt;border-top:none;border-left:
  none'>堆排序</td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N*log<font
  class="font88237"><sub>2</sub></font><font class="font68237">N)</font></td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N*log<font
  class="font88237"><sub>2</sub></font><font class="font68237">N)</font></td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N*log<font
  class="font88237"><sub>2</sub></font><font class="font68237">N)</font></td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(1)</td>
  <td class=xl658237 style='border-top:none;border-left:none'>不稳定</td>
 </tr>
 <tr height=22 style='height:16.5pt'>
  <td rowspan=2 height=44 class=xl638237 style='height:33.0pt;border-top:none'>交换排序</td>
  <td class=xl648237 style='border-top:none;border-left:none'>冒泡排序</td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N)</td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N<font
  class="font78237"><sup>2</sup></font><font class="font68237">)</font></td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N<font
  class="font78237"><sup>2</sup></font><font class="font68237">)</font></td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(1)</td>
  <td class=xl658237 style='border-top:none;border-left:none'>稳定</td>
 </tr>
 <tr height=22 style='height:16.5pt'>
  <td height=22 class=xl648237 style='height:16.5pt;border-top:none;border-left:
  none'>快速排序</td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N*log<font
  class="font88237"><sub>2</sub></font><font class="font68237">N)</font></td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N*log<font
  class="font88237"><sub>2</sub></font><font class="font68237">N)&nbsp;</font></td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N<font
  class="font78237"><sup>2</sup></font><font class="font68237">)</font></td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(log<font
  class="font88237"><sub>2</sub></font><font class="font68237">n)~O(n)</font></td>
  <td class=xl658237 style='border-top:none;border-left:none'>不稳定</td>
 </tr>
 <tr height=21 style='height:16.0pt'>
  <td colspan=2 height=21 class=xl638237 style='height:16.0pt'>归并排序</td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N*log<font
  class="font88237"><sub>2</sub></font><font class="font68237">N)&nbsp;</font></td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N*log<font
  class="font88237"><sub>2</sub></font><font class="font68237">N)&nbsp;</font></td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(N*log<font
  class="font88237"><sub>2</sub></font><font class="font68237">N)&nbsp;</font></td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(n)</td>
  <td class=xl658237 style='border-top:none;border-left:none'>稳定</td>
 </tr>
 <tr height=19 style='height:14.0pt'>
  <td colspan=2 height=19 class=xl638237 style='height:14.0pt'>基数排序·</td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(d(r+n))</td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(d(r+n))</td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(d(r+n))</td>
  <td class=xl658237 style='border-top:none;border-left:none'>O(rd+n)</td>
  <td class=xl658237 style='border-top:none;border-left:none'>稳定</td>
 </tr>
 <tr height=19 style='height:14.0pt'>
  <td colspan=7 height=19 class=xl668237 style='height:14.0pt'>注：r代表关键字基数，d代表长度，n代表关键字个数</td>
 </tr>
 <![if supportMisalignedColumns]>
 <tr height=0 style='display:none'>
  <td width=69 style='width:52pt'></td>
  <td width=69 style='width:52pt'></td>
  <td width=107 style='width:81pt'></td>
  <td width=109 style='width:82pt'></td>
  <td width=125 style='width:94pt'></td>
  <td width=99 style='width:74pt'></td>
  <td width=69 style='width:52pt'></td>
 </tr>
 <![endif]>
</table>

</div>


<!----------------------------->
<!--“从 EXCEL 发布网页”向导结束-->
<!----------------------------->
</body>

</html>


