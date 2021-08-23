# Register the DescendTreeExtra report addon

register(REPORT,
  id    = 'descend_tree_extra',
  name  = _("Descendent Tree with Extras"),
  description =  _("Produces a graphical report combining a descendant tree with three ancestor generations and stepchildren."),
  version = '1.0.0',
  gramps_target_version = '5.1',
  status = STABLE,
  fname = 'DescendTreeExtra.py',
  authors = ["Peter Zingg"],
  authors_email = ["peter.zingg@gmail.com"],
  category = CATEGORY_DRAW,
  require_active = True,
  reportclass = 'DescendTreeExtra',
  optionclass = 'DescendTreeExtraOptions',
  report_modes = [REPORT_MODE_GUI, REPORT_MODE_CLI],
)
