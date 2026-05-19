from odoo import models, fields


class TaskManagerTask(models.Model):
    _name = "task.manager.task"
    _description = "Task Manager Task"

    name = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description")
    deadline = fields.Date(string="Deadline")
    priority = fields.Selection([
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ], string="Priority", default="medium")
    state = fields.Selection([
        ("todo", "To Do"),
        ("in_progress", "In Progress"),
        ("done", "Done"),
    ], string="Status", default="todo")
