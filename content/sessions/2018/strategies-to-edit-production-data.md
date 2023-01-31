---
id: 
title: "Strategies to edit production data"
speakers:
 - julie-qiu
time_start: 2018-03-15T16:00:00-05:00
time_end: 2018-03-15T16:40:00-05:00
block: 
slot: 
---

At some point, we all find ourselves at a SQL prompt making edits to the production database. We know it’s a bad practice, and we always intend to put in place safer infrastructure before we need to do it again, but what does a better system actually look like?

This talk progresses through 5 strategies for teams using a Python stack to do SQL writes against a database, to achieve increasing safety and auditability:
<ul>
 	<li>Raw SQL queries</li>
 	<li>Local one-off scripts</li>
 	<li>Deploy and run scripts from an application server</li>
 	<li>Run scripts from Jenkins with command line arguments</li>
 	<li>Build a Script Runner application</li>
</ul>
We’ll talk about the pros and cons of each strategy, and help you determine which one is right for your specific needs.

By the end of this talk, you’ll be ready to start upgrading your infrastructure for making changes to your production database safely!