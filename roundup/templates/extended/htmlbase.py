 
# Do Not Edit (Unless You Want To)
# This file automagically generated by roundup.htmldata.makeHtmlBase
# 
fileDOTindex = """<!-- $Id: htmlbase.py,v 1.3 2001-07-30 01:26:59 richard Exp $-->
<tr>
    <property name="name">
        <td><display call="link('name')"></td>
    </property>
    <property name="type">
        <td><display call="plain('type')"></td>
    </property>
</tr>
"""

issueDOTfilter = """<!-- $Id: htmlbase.py,v 1.3 2001-07-30 01:26:59 richard Exp $-->
<property name="title">
 <tr><th width="1%" align="right" class="location-bar">Title</th>
 <td><display call="field('title')"></td></tr>
</property>
<property name="status">
 <tr><th width="1%" align="right" class="location-bar">Status</th>
 <td><display call="checklist('status')"></td></tr>
</property>
<property name="priority">
 <tr><th width="1%" align="right" class="location-bar">Priority</th>
 <td><display call="checklist('priority')"></td></tr>
</property>
<property name="platform">
 <tr><th width="1%" align="right" class="location-bar">Platform</th>
 <td><display call="checklist('platform')"></td></tr>
</property>
<property name="product">
 <tr><th width="1%" align="right" class="location-bar">Product</th>
 <td><display call="checklist('product')"></td></tr>
</property>
<property name="version">
 <tr><th width="1%" align="right" class="location-bar">Version</th>
 <td><display call="field('version')"></td></tr>
</property>
<property name="assignedto">
 <tr><th width="1%" align="right" class="location-bar">Assigned&nbsp;to</th>
 <td><display call="checklist('assignedto')"></td></tr>
</property>
"""

issueDOTindex = """<!-- $Id: htmlbase.py,v 1.3 2001-07-30 01:26:59 richard Exp $-->
<tr>
    <property name="id">
        <td valign="top"><display call="field('id')"></td>
    </property>
    <property name="activity">
        <td valign="top"><display call="reldate('activity', pretty=1)"></td>
    </property>
    <property name="priority">
        <td valign="top"><display call="plain('priority')"></td>
    </property>
    <property name="status">
        <td valign="top"><display call="plain('status')"></td>
    </property>
    <property name="title">
        <td valign="top"><display call="link('title')"></td>
    </property>
    <property name="platform">
        <td valign="top"><display call="plain('platform')"></td>
    </property>
    <property name="product">
        <td valign="top"><display call="plain('product')"></td>
    </property>
    <property name="version">
        <td valign="top"><display call="plain('version')"></td>
    </property>
    <property name="assignedto">
        <td valign="top"><display call="plain('assignedto')"></td>
    </property>
</tr>
"""

issueDOTitem = """<!-- $Id: htmlbase.py,v 1.3 2001-07-30 01:26:59 richard Exp $-->
<table border=0 cellspacing=0 cellpadding=2>

<tr class="strong-header">
  <td colspan=4>Item Information</td>
</td>

<tr  bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Title</span></td>
    <td colspan=3 class="form-text"><display call="field('title', size=80)"></td>
</tr>

<tr bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Product</span></td>
    <td class="form-text" valign=middle><display call="menu('product')">
    version:<display call="field('version', 5)"></td>
    <td width=1% nowrap align=right><span class="form-label">Platform</span></td>
    <td class="form-text" valign=middle><display call="checklist('platform')"></td>
</tr>

<tr bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Created</span></td>
    <td class="form-text"><display call="reldate('creation', pretty=1)">
        (<display call="plain('creator')">)</td>
    <td width=1% nowrap align=right><span class="form-label">Last activity</span></td>
    <td class="form-text"><display call="reldate('activity', pretty=1)"></td>
</tr>

<tr bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Priority</span></td>
    <td class="form-text"><display call="field('priority')"></td>
    <td width=1% nowrap align=right><span class="form-label">Status</span></td>
    <td class="form-text"><display call="menu('status')"></td>
</tr>

<tr bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Assigned To</span></td>
    <td class="form-text"><display call="field('assignedto')"></td>
    <td width=1% nowrap align=right><span class="form-label">Empty</span></td>
    <td class="form-text">XXXX</td>
</tr>

<tr bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Superseder</span></td>
    <td class="form-text"><display call="field('superseder', size=40, showid=1)"></td>
    <td width=1% nowrap align=right><span class="form-label">Nosy List</span></td>
    <td class="form-text"><display call="field('nosy')"></td>
</tr>

<tr bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Change Note</span></td>
    <td colspan=3 class="form-text"><display call="note()"></td>
</tr>

<tr bgcolor="ffffea">
    <td>&nbsp;</td>
    <td colspan=3 class="form-text"><display call="submit()"></td>
</tr>

<property name="messages">
<tr class="strong-header">
    <td colspan=4><b>Messages</b></td>
</tr>
<tr>            
    <td colspan=4><display call="list('messages')"></td>
</tr>
</property>

<property name="files">
 <tr class="strong-header">
     <td colspan=4><b>Files</b></td>
 </tr>
 <tr>            
     <td colspan=4><display call="list('files')"></td>
 </tr>
</property>

</table>

"""

msgDOTindex = """<!-- $Id: htmlbase.py,v 1.3 2001-07-30 01:26:59 richard Exp $-->
<tr>
    <property name="date">
        <td><display call="link('date')"></td>
    </property>
    <property name="author">
        <td><display call="plain('author')"></td>
    </property>
    <property name="summary">
        <td><display call="plain('summary')"></td>
    </property>
</tr>
"""

msgDOTitem = """<!-- $Id: htmlbase.py,v 1.3 2001-07-30 01:26:59 richard Exp $-->
<table border=0 cellspacing=0 cellpadding=2>

<tr class="strong-header">
  <td colspan=2>Message Information</td>
</td>

<tr bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Author</span></td>
    <td class="form-text"><display call="plain('author')"></td>
</tr>

<tr bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Recipients</span></td>
    <td class="form-text"><display call="plain('recipients')"></td>
</tr>

<tr bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Date</span></td>
    <td class="form-text"><display call="plain('date')"></td>
</tr>

<tr bgcolor="ffeaff">
 <td colspan=2 class="form-text">
  <pre><display call="plain('content')"></pre>
 </td>
</tr>

<property name="files">
<tr class="strong-header"><td colspan=2><b>Files</b></td></tr>
<tr><td colspan=2><display call="list('files')"></td></tr>
</property>

<tr class="strong-header"><td colspan=2><b>History</b></td><tr>
<tr><td colspan=2><display call="history()"></td></tr>

</table>
"""

styleDOTcss = """h1 {
  font-family: Verdana, Helvetica, sans-serif; 
  font-size: 18pt; 
  font-weight: bold; 
}

h2 {
  font-family: Verdana, Helvetica, sans-serif; 
  font-size: 16pt; 
  font-weight: bold; 
}

h3 {
  font-family: Verdana, Helvetica, sans-serif; 
  font-size: 12pt; 
  font-weight: bold; 
}

a:hover {  
  font-family: Verdana, Helvetica, sans-serif; 
  text-decoration: underline;
  color: #333333; 
}

a:link {
  font-family: Verdana, Helvetica, sans-serif; 
  text-decoration: none;
  color: #000099;
}

a {
  font-family: Verdana, Helvetica, sans-serif; 
  text-decoration: none;
  color: #000099;
}

p {
  font-family: Verdana, Helvetica, sans-serif;
  font-size: 10pt;
  color: #333333;
}

th {
  font-family: Verdana, Helvetica, sans-serif; 
  font-weight: bold;
  font-size: 10pt; 
  color: #333333;
}

.form-help {
  font-family: Verdana, Helvetica, sans-serif;
  font-size: 10pt;
  color: #333333;
}

.std-text {
  font-family: Verdana, Helvetica, sans-serif;
  font-size: 10pt;
  color: #333333;
}

.tab-small {
  font-family: Verdana, Helvetica, sans-serif; 
  font-size: 8pt; 
  color: #333333;
}

.location-bar {
  background-color: #efefef;
  border: none;
}

.strong-header {
  font-family: Verdana, Helvetica, sans-serif;
  font-size: 12pt;
  font-weight: bold;
  background-color: #000000;
  color: #ffffff;
}

.list-header {
  background-color: #c0c0c0;
  border: none;
}

.list-item {
  font-family: Verdana, Helvetica, sans-serif; 
  font-size: 10pt; 
}

.list-nav {
  font-family: Verdana, Helvetica, sans-serif; 
  font-size: 10pt; 
  font-weight: bold;
}

.row-normal {
  background-color: #ffffff;
  border: none;

}

.row-hilite {
  background-color: #efefef;
  border: none;
}

.section-bar {
  background-color: #c0c0c0;
  border: none;
}

.system-msg {
  font-family: Verdana, Helvetica, sans-serif; 
  font-size: 10pt; 
  background-color: #ffffff;
  border:  1px solid #000000;
  margin-bottom: 6px;
  margin-top: 6px;
  padding: 4px;
  width: 100%;
  color: #660033;
}

.form-title {
  font-family: Verdana, Helvetica, sans-serif; 
  font-weight: bold;
  font-size: 12pt; 
  color: #333333;
}

.form-label {
  font-family: Verdana, Helvetica, sans-serif; 
  font-weight: bold;
  font-size: 10pt; 
  color: #333333;
}

.form-optional {
  font-family: Verdana, Helvetica, sans-serif; 
  font-weight: bold;
  font-style: italic;
  font-size: 10pt; 
  color: #333333;
}

.form-element {
  font-family: Verdana, Helvetica, aans-serif;
  font-size: 10pt;
  color: #000000;
}

.form-text {
  font-family: Verdana, Helvetica, sans-serif;
  font-size: 10pt;
  color: #333333;
}

.form-mono {
  font-family: monospace;
  font-size: 12px;
  text-decoration: none;
}
"""

supportDOTfilter = """<!-- $Id: htmlbase.py,v 1.3 2001-07-30 01:26:59 richard Exp $-->
<property name="title">
 <tr><th width="1%" align="right" class="location-bar">Title</th>
 <td><display call="field('title')"></td></tr>
</property>
<property name="status">
 <tr><th width="1%" align="right" class="location-bar">Status</th>
 <td><display call="checklist('status')"></td></tr>
</property>
<property name="platform">
 <tr><th width="1%" align="right" class="location-bar">Platform</th>
 <td><display call="checklist('platform')"></td></tr>
</property>
<property name="product">
 <tr><th width="1%" align="right" class="location-bar">Product</th>
 <td><display call="checklist('product')"></td></tr>
</property>
<property name="version">
 <tr><th width="1%" align="right" class="location-bar">Version</th>
 <td><display call="field('version')"></td></tr>
</property>
<property name="source">
 <tr><th width="1%" align="right" class="location-bar">Source</th>
 <td><display call="checklist('source')"></td></tr>
</property>
<property name="assignedto">
 <tr><th width="1%" align="right" class="location-bar">Assigned&nbsp;to</th>
 <td><display call="checklist('assignedto')"></td></tr>
</property>
<property name="customername">
 <tr><th width="1%" align="right" class="location-bar">Customer&nbsp;name</th>
 <td><display call="field('customername')"></td></tr>
</property>
"""

supportDOTindex = """<!-- $Id: htmlbase.py,v 1.3 2001-07-30 01:26:59 richard Exp $-->
<tr>
    <property name="id">
        <td valign="top"><display call="field('id')"></td>
    </property>
    <property name="activity">
        <td valign="top"><display call="reldate('activity', pretty=1)"></td>
    </property>
    <property name="status">
        <td valign="top"><display call="plain('status')"></td>
    </property>
    <property name="title">
        <td valign="top"><display call="link('title')"></td>
    </property>
    <property name="platform">
        <td valign="top"><display call="plain('platform')"></td>
    </property>
    <property name="product">
        <td valign="top"><display call="plain('product')"></td>
    </property>
    <property name="version">
        <td valign="top"><display call="plain('version')"></td>
    </property>
    <property name="source">
        <td valign="top"><display call="plain('source')"></td>
    </property>
    <property name="assignedto">
        <td valign="top"><display call="plain('assignedto')"></td>
    </property>
    <property name="customername">
        <td valign="top"><display call="plain('customername')"></td>
    </property>
</tr>
"""

supportDOTitem = """<!-- $Id: htmlbase.py,v 1.3 2001-07-30 01:26:59 richard Exp $-->
<table border=0 cellspacing=0 cellpadding=2>

<tr class="strong-header">
  <td colspan=4>Item Information</td>
</td>

<tr  bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Title</span></td>
    <td colspan=3 class="form-text"><display call="field('title', size=80)"></td>
</tr>

<tr bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Product</span></td>
    <td class="form-text" valign=middle><display call="menu('product')">
    version:<display call="field('version', 5)"></td>
    <td width=1% nowrap align=right><span class="form-label">Platform</span></td>
    <td class="form-text" valign=middle><display call="checklist('platform')"></td>
</tr>

<tr bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Created</span></td>
    <td class="form-text"><display call="reldate('creation', pretty=1)">
        (<display call="plain('creator')">)</td>
    <td width=1% nowrap align=right><span class="form-label">Last activity</span></td>
    <td class="form-text"><display call="reldate('activity', pretty=1)"></td>
</tr>

<tr bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Empty</span></td>
    <td class="form-text">XXXX</td>
    <td width=1% nowrap align=right><span class="form-label">Source</span></td>
    <td class="form-text"><display call="field('source')"></td>
</tr>

<tr bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Status</span></td>
    <td class="form-text"><display call="menu('status')"></td>
    <td width=1% nowrap align=right><span class="form-label">Rate</span></td>
    <td class="form-text"><display call="field('rate')"></td>
</tr>

<tr bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Assigned To</span></td>
    <td class="form-text"><display call="field('assignedto')"></td>
    <td width=1% nowrap align=right><span class="form-label">Customer Name</span></td>
    <td class="form-text"><display call="field('customername')"></td>
</tr>

<tr bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Superseder</span></td>
    <td class="form-text"><display call="field('superseder', size=40, showid=1)"></td>
    <td width=1% nowrap align=right><span class="form-label">Nosy List</span></td>
    <td class="form-text"><display call="field('nosy')"></td>
</tr>

<tr bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Change Note</span></td>
    <td colspan=3 class="form-text"><display call="note()"></td>
</tr>

<tr bgcolor="ffffea">
    <td>&nbsp;</td>
    <td colspan=3 class="form-text"><display call="submit()"></td>
</tr>

<property name="messages">
<tr class="strong-header">
    <td colspan=4><b>Messages</b></td>
</tr>
<tr>            
    <td colspan=4><display call="list('messages')"></td>
</tr>
</property>

<property name="files">
 <tr class="strong-header">
     <td colspan=4><b>Files</b></td>
 </tr>
 <tr>            
     <td colspan=4><display call="list('files')"></td>
 </tr>
</property>

</table>

"""

userDOTindex = """<!-- $Id: htmlbase.py,v 1.3 2001-07-30 01:26:59 richard Exp $-->
<tr>
    <property name="username">
        <td><display call="link('username')"></td>
    </property>
    <property name="realname">
        <td><display call="plain('realname')"></td>
    </property>
    <property name="organisation">
        <td><display call="plain('organisation')"></td>
    </property>
    <property name="address">
        <td><display call="plain('address')"></td>
    </property>
    <property name="phone">
        <td><display call="plain('phone')"></td>
    </property>
</tr>
"""

userDOTitem = """<!-- $Id: htmlbase.py,v 1.3 2001-07-30 01:26:59 richard Exp $-->
<table border=0 cellspacing=0 cellpadding=2>

<tr class="strong-header">
  <td colspan=2>Your Details</td>
</td>

<tr  bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Name</span></td>
    <td class="form-text"><display call="field('realname', size=40)"></td>
</tr>
<tr  bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Login Name</span></td>
    <td class="form-text"><display call="field('username', size=40)"></td>
</tr>
<tr  bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Login Password</span></td>
    <td class="form-text"><display call="field('password', size=10)"></td>
</tr>
<tr  bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Phone</span></td>
    <td class="form-text"><display call="field('phone', size=40)"></td>
</tr>
<tr  bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">Organisation</span></td>
    <td class="form-text"><display call="field('organisation', size=40)"></td>
</tr>
<tr  bgcolor="ffffea">
    <td width=1% nowrap align=right><span class="form-label">E-mail address</span></td>
    <td class="form-text"><display call="field('address', size=40)"></td>
</tr>

<tr bgcolor="ffffea">
    <td>&nbsp;</td>
    <td class="form-text"><display call="submit()"></td>
</tr>

<tr class="strong-header">
    <td colspan=2><b>History</b></td>
</tr>
<tr>
    <td colspan=2><display call="history()"></td>
</tr>

</table>

"""

