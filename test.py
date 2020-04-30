from locust import HttpLocust, TaskSet, task


class UserBehavior(TaskSet):
    # 初始化
    def on_start(self):
        self.users_index = 0  # 设置user参数下标的初始值
        self.groups_index = 0  # 设置group参数下标的初始值

    @task
    def test_users(self):
        users_id = self.locust.uid[self.users_index]  # 读取uid参数
        url = '/users/' + str(users_id) + '/'
        self.client.get(url, auth=('admin', 'admin123'))
        # 取余运算，循环遍历参数（下标：0,1,2,3,0,1,2,3...）
        self.users_index = (self.users_index + 1) % len(self.locust.uid)

    @task
    def test_groups(self):
        groups_id = self.locust.gid[self.groups_index]  # 读取gid参数
        url = '/groups/' + str(groups_id) + '/'
        self.client.get(url, auth=('admin', 'admin123'))
        self.groups_index = (self.groups_index + 1) % len(self.locust.gid)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    # 参数配置
    uid = [1, 2, 3, 4]
    gid = [1, 2]
    min_wait = 3000
    max_wait = 6000
    host = 'http://127.0.0.1:8000'  # 设置Host