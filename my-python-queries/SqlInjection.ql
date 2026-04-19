import python

from Call call
where call.toString().regexpMatch(".*execute.*")
select call, "Possible SQL Injection found here."
