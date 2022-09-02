from abc import ABCMeta, abstractmethod

from enums.BranchStatus import BranchStatus


class BranchInterface(metaclass=ABCMeta):
    @abstractmethod
    def add_branch(self, branch_name):
        pass

    @abstractmethod
    def update_branch_status(self, branch_name, branch_status: BranchStatus):
        pass

