# Тип теста
test_type = 10

# Список сенсоров
sensors = ['sensor_37', 'sensor_03', 'sensor_28', 'sensor_31', 'sensor_50', 'sensor_01', 'sensor_14', 'sensor_30',
           'sensor_32', 'sensor_18', 'sensor_11', 'sensor_49', 'sensor_34', 'sensor_42', 'sensor_21', 'sensor_05',
           'sensor_16', 'sensor_24', 'sensor_39', 'sensor_44']

all_data_dict = {
    'sensor_37': {
        'data': ['5cf6c0', '4f75f6', 'aa19cb', '12bab5', '104542', '278605', '195646', '1eef92', '624716', '67143a'],
        'time': 1.86},
    'sensor_03': {
        'data': ['c8050e', 'ed40ef', '171cc2', '784d63', '8b34fa', '781359', '331a3e', 'd13a32', 'e97cc3', '1667ba'],
        'time': 2.96},
    'sensor_28': {
        'data': ['d2595c', '78740f', '8f3507', 'ea78d6', 'ebc569', '3818c4', 'fa1f6c', '5fc388', '025779', '8592fb'],
        'time': 1.04},
    'sensor_31': {
        'data': ['67efee', '091f4f', '87fd73', '12742b', 'c9c2de', 'd81a22', '5343cf', '4b0ab0', '1468eb', '41e493'],
        'time': 0.57},
    'sensor_50': {
        'data': ['106bfe', '76817d', 'aa21d4', '5f126b', '8e1997', '0f2e21', '33bbb4', '4309d2', '564a93', '0241d4'],
        'time': 1.31},
    'sensor_01': {
        'data': ['a043ba', 'e16038', '03a839', 'c0cb52', 'f511d9', 'cb8f68', 'd9d9b0', '341314', 'a5534e', 'a92b26'],
        'time': 2.97},
    'sensor_14': {
        'data': ['d4c6e8', 'd449f7', '285887', '53b93c', '0bbc6a', 'df7089', 'dd787b', '6a27f5', 'baddd6', '5bcd01'],
        'time': 1.97},
    'sensor_30': {
        'data': ['43b55e', 'c41a6f', 'dfc44b', '574738', 'eb2993', 'a8a06b', '1c08e6', 'ee73f5', 'ae198b', 'ee2e2e'],
        'time': 2.99},
    'sensor_32': {
        'data': ['2b9687', '8a33cd', '17b190', '889258', '13918c', '78707c', 'b6db90', '51fe1e', '06ccfa', '6f6de6'],
        'time': 2.11},
    'sensor_18': {
        'data': ['520b8b', '7c818f', '0cd87f', '076a7e', '11914a', '85f879', '1bdacb', '373576', '16a52e', '1d11bc'],
        'time': 1.76}, 'sensor_11': {
        'data': ['b49786', 'b5b441', '318c23', '7bf841', '332084', 'f8b2d7', 'd97720', 'f7d61a', '0294f1', 'c9c387'],
        'time': 1.44},
    'sensor_49': {
        'data': ['bed509', 'ecddf5', 'f61422', 'fcfa2f', 'bec392', '4b2bff', '6ff09e', 'f39e2b', '3f2e1b', 'ae7431'],
        'time': 0.92},
    'sensor_34': {
        'data': ['ac5626', 'c7d4bc', 'e8f823', '3aed1b', '34a9d3', 'cb87d5', 'f0ef1f', '7393e8', 'c68548', '71f7de'],
        'time': 1.24},
    'sensor_42': {
        'data': ['a79467', 'ae184e', '5f50cb', 'b7a518', '3634d5', '9975a0', '1c71d7', '0f3b2a', '2e4a45', 'e264b3'],
        'time': 2.04},
    'sensor_21': {
        'data': ['9ca2c7', 'cc7e9a', '9da217', '440847', '0d1dd9', '878ce7', 'ca5720', '1e5b82', '377825', '4659ca'],
        'time': 0.38},
    'sensor_05': {
        'data': ['3b36a4', '5c17ff', '134eee', '52db9f', 'a0d4af', '211849', 'b3a47e', 'd1640c', 'a4b860', '1ee8d9'],
        'time': 0.61},
    'sensor_16': {
        'data': ['5a9aba', 'daea47', '9b14b2', '28f8ed', '4d7cb5', '1f2fdb', 'ffc5c0', '87aa9d', 'f130e8', 'e31de4'],
        'time': 1.34},
    'sensor_24': {
        'data': ['c71e90', '832693', '6a1f18', '8f867a', 'f40c5b', 'acb508', 'd2c7ba', 'c1c740', '30e8f8', '4c35cd'],
        'time': 1.13},
    'sensor_39': {
        'data': ['1ca5a0', 'fa6cf6', '048899', '76c985', '016f1f', '247377', '7b54c1', 'daa2f3', '228f36', '2a6093'],
        'time': 1.86},
    'sensor_44': {
        'data': ['798ffe', '2d95ac', 'fc0140', '0c8a86', 'b18944', '83c86a', 'da1bbd', '016794', 'bb1bb2', 'f8cb22'],
        'time': 2.39}
}


# Имитация space_time(sensor_name)
def space_time(sensor_name):
    return all_data_dict[sensor_name]['time']  # для 'sensor_39' будет возвращено 1.86


# имитация space_data(sensor_name)
def space_data(sensor_name):
    return all_data_dict[sensor_name]['data']  # для 'sensor_39' будет возвращено
    # ['1ca5a0', 'fa6cf6', '048899', '76c985', '016f1f', '247377', '7b54c1', 'daa2f3', '228f36', '2a6093']


import asyncio


async def sensor_data(sensor_name):
    # Ожидание времени, полученного от space_time
    await asyncio.sleep(space_time(sensor_name))

    # Получение и обработка данных
    data_values = space_data(sensor_name)
    processed_data = ''.join(data_values)

    # Формирование строки отчета
    report_line = f"{sensor_name}_data: {processed_data}"

    return report_line


async def main():
    # Создание списка задач на опрос сенсоров
    tasks = [sensor_data(sensor) for sensor in sensors]

    # Асинхронный запуск и ожидание результатов
    results = await asyncio.gather(*tasks)

    # Формирование отчета, включая информацию о типе теста
    report = [f"Результаты проведения теста типа {test_type}:"]
    report.extend(sorted(results))  # Сортировка по возрастанию номера сенсора

    return report


# Запуск основной программы
if __name__ == "__main__":
    result = asyncio.run(main())

    # Добавьте assert для проверки результата
    assert result == [
        'Результаты проведения теста типа 10:',
        'sensor_01_data: a043bae1603803a839c0cb52f511d9cb8f68d9d9b0341314a5534ea92b26',
        'sensor_03_data: c8050eed40ef171cc2784d638b34fa781359331a3ed13a32e97cc31667ba',
        'sensor_05_data: 3b36a45c17ff134eee52db9fa0d4af211849b3a47ed1640ca4b8601ee8d9',
        'sensor_11_data: b49786b5b441318c237bf841332084f8b2d7d97720f7d61a0294f1c9c387',
        'sensor_14_data: d4c6e8d449f728588753b93c0bbc6adf7089dd787b6a27f5baddd65bcd01',
        'sensor_16_data: 5a9abadaea479b14b228f8ed4d7cb51f2fdbffc5c087aa9df130e8e31de4',
        'sensor_18_data: 520b8b7c818f0cd87f076a7e11914a85f8791bdacb37357616a52e1d11bc',
        'sensor_21_data: 9ca2c7cc7e9a9da2174408470d1dd9878ce7ca57201e5b823778254659ca',
        'sensor_24_data: c71e908326936a1f188f867af40c5bacb508d2c7bac1c74030e8f84c35cd',
        'sensor_28_data: d2595c78740f8f3507ea78d6ebc5693818c4fa1f6c5fc3880257798592fb',
        'sensor_30_data: 43b55ec41a6fdfc44b574738eb2993a8a06b1c08e6ee73f5ae198bee2e2e',
        'sensor_31_data: 67efee091f4f87fd7312742bc9c2ded81a225343cf4b0ab01468eb41e493',
        'sensor_32_data: 2b96878a33cd17b19088925813918c78707cb6db9051fe1e06ccfa6f6de6',
        'sensor_34_data: ac5626c7d4bce8f8233aed1b34a9d3cb87d5f0ef1f7393e8c6854871f7de',
        'sensor_37_data: 5cf6c04f75f6aa19cb12bab51045422786051956461eef9262471667143a',
        'sensor_39_data: 1ca5a0fa6cf604889976c985016f1f2473777b54c1daa2f3228f362a6093',
        'sensor_42_data: a79467ae184e5f50cbb7a5183634d59975a01c71d70f3b2a2e4a45e264b3',
        'sensor_44_data: 798ffe2d95acfc01400c8a86b1894483c86ada1bbd016794bb1bb2f8cb22',
        'sensor_49_data: bed509ecddf5f61422fcfa2fbec3924b2bff6ff09ef39e2b3f2e1bae7431',
        'sensor_50_data: 106bfe76817daa21d45f126b8e19970f2e2133bbb44309d2564a930241d4'
    ]

    print("All tests passed!")
