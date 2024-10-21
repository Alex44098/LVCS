from Views import ProjectChooserView
from Controllers import ProjectChooserController

view = ProjectChooserView.LVCSView()
controller = ProjectChooserController.ProjectChooserController(None, view)

view.set_ctrl(controller)

view.mainloop()
