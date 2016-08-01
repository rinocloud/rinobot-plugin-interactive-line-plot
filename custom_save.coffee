_ = require "underscore"
props = require "core/properties"
ActionTool = require "models/tools/actions/action_tool"

class CustomSaveToolView extends ActionTool.View
  do: () ->
    canvas = @plot_view.get_canvas_element()
    curFile = location.pathname.split('/')[location.pathname.split('/').length-1]
    ext = curFile.substr(curFile.lastIndexOf('.')+1)
    name = curFile.replace(ext, 'png')

    if canvas.msToBlob?
      blob = canvas.msToBlob()
      window.navigator.msSaveBlob(blob, name)
    else
      link = document.createElement('a')
      link.href = canvas.toDataURL('image/png')
      link.download = name
      link.target = "_blank"
      link.dispatchEvent(new MouseEvent('click'))

class CustomSaveTool extends ActionTool.Model
  default_view: CustomSaveToolView
  type: "CustomSaveTool"
  tool_name: "Save"
  icon: "bk-tool-icon-save"

module.exports =
  Model: CustomSaveTool
  View: CustomSaveToolView
