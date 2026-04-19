/**
 * @name SQL Injection Detection
 * @kind problem
 * @severity error
 */

import python

from Call call, Attribute attr
where
  call.getFunc() = attr and
  attr.getName() = "execute"
select call, "Possible SQL Injection: direct use of execute() detected."
