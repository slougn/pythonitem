#!/usr/bin/env python
# coding=utf-8
'''
Author: 560130
Date: 2021-12-27 22:51:46
LastEditTime: 2021-12-27 23:34:16
LastEditors: 560130
Description: 用来保存Class note 和 Class notebook类
FilePath: /pythonitem/object-orientedProgrammingPy/chapter2/parent_directory/notebook.py
'''


import datetime
# 为所有的新笔记存储下一个可用id
last_id = 0


class Note:
    '''
    description:Represent a note in the notebook. Match
                against a string in searches and store tags for each note.
    param {*}
    return {*}
    '''

    def __init__(self, memo, tags='') -> None:
        '''
        description:initialize a note with memo and optional
                    space-separated tags.Automatically set
                    the note's creation date and a unique id.
        param {*}
        return {None}
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id  # 只是说有一个全局的变量，变量在此之外
        last_id = last_id + 1
        self.id = last_id

    def match(self, filter):
        '''
        description:Determine if this note matches the filter text.
                    Return True if it matches,False otherwise.
                    Serch is case sensitive and matches both text and tags.
        param {*}
        return:filter in self.memo or filter in self.tags
        '''
        pass  # 还没有实现


class Notebook:
    '''
    description: represent a collection of notes that can be tagged,
                 modified,and serched.
    '''

    def __init__(self) -> None:
        '''
        description:Initialize a notebook with an empty list.
        param {*}
        return {*}
        '''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''
        description:Create a new note and add it to the list.
        param {*}
        return {*}
        '''
        self.notes.append(Note(memo, tags))

    def modify_memo(self, note_id, memo):
        '''
        description:Find the note with the given id and change its
                    memo to the given value.
        param {*}
        return {*}
        '''
        for note in self.notes:
            if note.id == note_id:
                note.memo = memo
                break

    def modify_tags(self, note_id, tags):
        '''
        description:Find the note with the given id and change its
                    tags to the given value.
        param {*}
        return {*}
        '''
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter):
        '''
        description:Find all notes that match the given filter string
        return {*}
        '''
        return [note for note in self.notes if note.match(filter)]

    pass


if __name__ == "__main__":
    n1 = Note("hello first")
    n2 = Note("hello again")

    print(n1.id)
    print(n2.id)

    n1.match('hello')
    n2.match('second')

    n = Notebook()
    n.new_note("hello world")
    n.new_note("hello again")

    print(n.notes)
    print(n.notes[0].id)
    print(n.notes[1].id)
    print(n.notes[0].memo)
    print(n.search("world"))
    print(n.modify_memo(1, "hi world"))
    print(n.notes[0].memo)
