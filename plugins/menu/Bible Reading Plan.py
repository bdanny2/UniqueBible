import config
from qtpy.QtWidgets import QWidget


class BibleReadingPlan(QWidget):

    template = {
        # Source / credits of the following plan: https://www.biblica.com/resources/reading-plans/
        1: [False, "Genesis 1, Genesis 2:1-17, Matthew 1:1-25, Psalm 1:1-6"],
        2: [False, "Genesis 2:18-25, Genesis 3, Genesis 4:1-16, Matthew 2:1-18, Psalm 2:1-12"],
        3: [False, "Genesis 4:17-26, Genesis 5, Genesis 6, Matthew 2:19-23, Matthew 3, Psalm 3:1-8"],
        4: [False, "Genesis 7, Genesis 8, Genesis 9:1-17, Matthew 4:1-22, Proverbs 1:1-7"],
        5: [False, "Genesis 9:18-29, Genesis 10, Genesis 11:1-9, Matthew 4:23-25, Matthew 5:1-20, Psalm 4:1-8"],
        6: [False, "Genesis 11:10-32, Genesis 12, Genesis 13, Matthew 5:21-42, Psalm 5:1-12"],
        7: [False, "Genesis 14, Genesis 15, Genesis 16, Matthew 5:43-48, Matthew 6:1-24, Psalm 6"],
        8: [False, "Genesis 17, Genesis 18, Matthew 6:25-34, Matthew 7:1-23, Proverbs 1:8-19"],
        9: [False, "Genesis 19, Genesis 20:1-18, Matthew 7:24-29, Matthew 8:1-22, Psalm 7:1-9"],
        10: [False, "Genesis 21, Genesis 22, Genesis 23, Matthew 8:23-34, Matthew 9:1-13, Psalm 7:10-17"],
        11: [False, "Genesis 24:1-67, Matthew 9:14-38, Psalm 8:1-9"],
        12: [False, "Genesis 25, Genesis 26, Matthew 10:1-31, Proverbs 1:20-33"],
        13: [False, "Genesis 27, Genesis 28:1-22, Matthew 10:32-42, Matthew 11:1-15, Psalm 9:1-6"],
        14: [False, "Genesis 29, Genesis 30, Matthew 11:16-30, Psalm 9:7-12"],
        15: [False, "Genesis 31:1-55, Matthew 12:1-21, Psalm 9:13-20"],
        16: [False, "Genesis 32, Genesis 33, Matthew 12:22-45, Proverbs 2:1-11"],
        17: [False, "Genesis 34, Genesis 35, Matthew 12:46-50, Matthew 13:1-17, Psalm 10:1-11"],
        18: [False, "Genesis 36, Genesis 37, Matthew 13:18-35, Psalm 10:12-18"],
        19: [False, "Genesis 38, Genesis 39, Matthew 13:36-58, Psalm 11:1-7"],
        20: [False, "Genesis 40, Genesis 41:1-40, Matthew 14:1-21, Proverbs 2:12-22"],
        21: [False, "Genesis 41:41-57, Genesis 42, Matthew 14:22-36, Matthew 15:1-9, Psalm 12:1-8"],
        22: [False, "Genesis 43, Genesis 44, Matthew 15:10-39, Psalm 13:1-6"],
        23: [False, "Genesis 45, Genesis 46, Genesis 47:1-12, Matthew 16:1-20, Psalm 14:1-7"],
        24: [False, "Genesis 47:13-31, Genesis 48, Matthew 16:21-28, Matthew 17:1-13, Proverbs 3:1-10"],
        25: [False, "Genesis 49, Genesis 50, Matthew 17:14-27, Matthew 18:1-9, Psalm 15:1-5"],
        26: [False, "Job 1, Job 2, Job 3, Matthew 18:10-35, Psalm 16:1-11"],
        27: [False, "Job 4, Job 5, Job 6, Job 7, Matthew 19:1-15, Psalm 17:1-5"],
        28: [False, "Job 8, Job 9, Job 10, Matthew 19:16-30, Proverbs 3:11-20"],
        29: [False, "Job 11, Job 12, Job 13, Job 14, Matthew 20:1-19, Psalm 17:6-12"],
        30: [False, "Job 15, Job 16, Job 17, Job 18, Matthew 20:20-34, Psalm 17:13-15"],
        31: [False, "Job 19, Job 20, Job 21, Matthew 21:1-17, Psalm 18:1-6"],
        32: [False, "Job 22, Job 23, Job 24, Matthew 21:18-32, Proverbs 3:21-35"],
        33: [False, "Job 25, Job 26, Job 27, Job 28, Job 29, Matthew 21:33-46, Matthew 22:1-14, Psalm 18:7-15"],
        34: [False, "Job 30, Job 31, Job 32, Matthew 22:15-46, Psalm 18:16-24"],
        35: [False, "Job 33, Job 34, Matthew 23:1-39, Psalm 18:25-36"],
        36: [False, "Job 35, Job 36, Job 37, Matthew 24:1-31, Proverbs 4:1-9"],
        37: [False, "Job 38, Job 39, Job 40:1-2, Matthew 24:32-51, Matthew 25:1-13, Psalm 18:37-42"],
        38: [False, "Job 40:3-24, Job 41, Job 42, Matthew 25:14-46, Psalm 18:43-50"],
        39: [False, "Exodus 1, Exodus 2, Exodus 3, Matthew 26:1-30, Psalm 19:1-6"],
        40: [False, "Exodus 4, Exodus 5, Exodus 6:1-12, Matthew 26:31-46, Proverbs 4:10-19"],
        41: [False, "Exodus 6:13-30, Exodus 7,Exodus 8, Matthew 26:47-68, Psalm 19:7-14"],
        42: [False, "Exodus 9, Exodus 10, Matthew 26:69-75, Matthew 27:1-10, Psalm 20:1-9"],
        43: [False, "Exodus 11, Exodus 12, Matthew 27:11-44, Psalm 21:1-7"],
        44: [False, "Exodus 13, Exodus 14, Matthew 27:45-66, Proverbs 4:20-27"],
        45: [False, "Exodus 15, Exodus 16, Matthew 28:1-20, Psalm 21:8-13"],
        46: [False, "Exodus 17, Exodus 18, Mark 1:1-28, Psalm 22:1-11"],
        47: [False, "Exodus 19, Exodus 20, Mark 1:29-45, Mark 2:1-17, Psalm 22:12-21"],
        48: [False, "Exodus 21, Exodus 22, Mark 2:18-27, Mark 3:1-30, Proverbs 5:1-14"],
        49: [False, "Exodus 23, Exodus 24, Mark 3:31-35, Mark 4:1-29, Psalm 22:22-31"],
        50: [False, "Exodus 25, Exodus 26, Mark 4:30-41, Mark 5:1-20, Psalm 23:1-6"],
        51: [False, "Exodus 27, Exodus 28, Mark 5:21-43, Mark 6:1-6, Psalm 24:1-10"],
        52: [False, "Exodus 29, Exodus 30, Mark 6:7-29, Proverbs 5:15-23"],
        53: [False, "Exodus 31, Exodus 32, Exodus 33:1-6, Mark 6:30-56, Psalm 25:1-7"],
        54: [False, "Exodus 33:7-23, Exodus 34, Mark 7:1-30, Psalm 25:8-15"],
        55: [False, "Exodus 35, Exodus 36, Mark 7:31-37, Mark 8:1-13, Psalm 25:16-22"],
        56: [False, "Exodus 37, Exodus 38, Mark 8:14-38, Mark 9:1, Proverbs 6:1-11"],
        57: [False, "Exodus 39, Exodus 40, Mark 9:2-32, Psalm 26:1-12"],
        58: [False, "Leviticus 1, Leviticus 2, Leviticus 3, Mark 9:33-50, Mark 10:1-12, Psalm 27:1-6"],
        59: [False, "Leviticus 4, Leviticus 5:1-13, Mark 10:13-31, Psalm 27:7-14"],
        60: [False, "Leviticus 5:14-19, Leviticus 6, Leviticus 7:1-10, Mark 10:32-52, Proverbs 6:12-19"],
        61: [False, "Leviticus 7:11-38, Leviticus 8, Mark 11:1-27, Psalm 28"],
        62: [False, "Leviticus 9, Leviticus 10, Mark 11:28-33, Mark 12:1-12, Psalm 29"],
        63: [False, "Leviticus 11, Leviticus 12, Mark 12:13-27, Psalm 30:1-7"],
        64: [False, "Leviticus 13:1-59, Mark 12:28-44, Proverbs 6:20-29"],
        65: [False, "Leviticus 14:1-57, Mark 13:1-31, Psalm 30:8-12"],
        66: [False, "Leviticus 15, Leviticus 16, Mark 13:32-37, Mark 14:1-16, Psalm 31:1-8"],
        67: [False, "Leviticus 17, Leviticus 18, Mark 14:17-42, Psalm 31:9-18"],
        68: [False, "Leviticus 19, Leviticus 20, Mark 14:43-72, Proverbs 6:30-35"],
        69: [False, "Leviticus 21, Leviticus 22, Mark 15:1-32, Psalm 31:19-24"],
        70: [False, "Leviticus 23, Leviticus 24, Mark 15:33-47, Psalm 32"],
        71: [False, "Leviticus 25, Leviticus 26:1-13, Mark 16:1-20, Psalm 33:1-11"],
        72: [False, "Leviticus 26:14-46, Leviticus 27, Luke 1:1-25, Proverbs 7:1-5"],
        73: [False, "Numbers 1, Numbers 2:1-9, Luke 1:26-38, Psalm 33:12-22"],
        74: [False, "Numbers 2:10-34, Numbers 3, Luke 1:39-56, Psalm 34:1-10"],
        75: [False, "Numbers 4, Numbers 5:1-10, Luke 1:57-80, Psalm 34:11-22"],
        76: [False, "Numbers 5:11-31, Numbers 6:1-27, Luke 2:1-20, Proverbs 7:6-20"],
        77: [False, "Numbers 7:1-65, Luke 2:21-40, Psalm 35:1-10"],
        78: [False, "Numbers 7:66-89, Numbers 8, Numbers 9:1-14, Luke 2:41-52, Psalm 35:11-18"],
        79: [False, "Numbers 9:15-23, Numbers 10, Numbers 11:1-3, Luke 3:1-22, Psalm 35:19-28"],
        80: [False, "Numbers 11:4-35, Numbers 12, Numbers 13:1-25, Luke 3:23-38, Luke 4:1-13, Proverbs 7:21-27"],
        81: [False, "Numbers 13:26-33, Numbers 14, Luke 4:14-37, Psalm 36:1-12"],
        82: [False, "Numbers 15, Numbers 16:1-35, Luke 4:38-44, Luke 5:1-16, Psalm 37:1-9"],
        83: [False, "Numbers 16:36-50, Numbers 17, Numbers 18, Luke 5:17-32, Psalm 37:10-20"],
        84: [False, "Numbers 19, Numbers 20, Numbers 21:1-3, Luke 5:33-39, Luke 6:1-11, Proverbs 8:1-11"],
        85: [False, "Numbers 21:4-35, Numbers 22:1-20, Luke 6:12-36, Psalm 37:21-31"],
        86: [False, "Numbers 22:21-41, Numbers 23:1-26, Luke 6:37-49, Luke 7:1-10, Psalm 37:32-40"],
        87: [False, "Numbers 23:27-30, Numbers 24, Numbers 25, Luke 7:11-35, Psalm 38:1-11"],
        88: [False, "Numbers 26, Numbers 27:1-11, Luke 7:36-50, Proverbs 8:12-21"],
        89: [False, "Numbers 27:12-23, Numbers 28, Numbers 29:1-11, Luke 8:1-18, Psalm 38:12-22"],
        90: [False, "Numbers 29:12-40, Numbers 30, Numbers 31:1-24, Luke 8:19-39, Psalm 39:1-13"],
        91: [False, "Numbers 31:25-54, Numbers 32, Luke 8:40-56, Luke 9:1-9, Psalm 40:1-8"],
        92: [False, "Numbers 33, Numbers 34, Luke 9:10-27, Proverbs 8:22-31"],
        93: [False, "Numbers 35, Numbers 36:1-12, Luke 9:28-56, Psalm 40:9-17"],
        94: [False, "Deuteronomy 1, Deuteronomy 2:1-23, Luke 9:57-62, Luke 10:1-24, Psalm 41:1-6"],
        95: [False, "Deuteronomy 2:24-37, Deuteronomy 3, Deuteronomy 4:1-14, Luke 10:25-42, Luke 11:1-4, Psalm 41:7-13"],
        96: [False, "Deuteronomy 4:15-49, Deuteronomy 5, Luke 11:5-32, Proverbs 8:32-36"],
        97: [False, "Deuteronomy 6, Deuteronomy 7, Deuteronomy 8, Luke 11:33-54, Psalm 42:1-6"],
        98: [False, "Deuteronomy 9, Deuteronomy 10, Luke 12:1-34, Psalm 42:7-11"],
        99: [False, "Deuteronomy 11, Deuteronomy 12, Luke 12:35-59, Psalm 43:1-5"],
        100: [False, "Deuteronomy 13, Deuteronomy 14, Luke 13:1-30, Proverbs 9:1-12"],
        101: [False, "Deuteronomy 15, Deuteronomy 16:1-20, Luke 13:31-35, Luke 14:1-14, Psalm 44:1-12"],
        102: [False, "Deuteronomy 16:21-22, Deuteronomy 17, Deuteronomy 18, Luke 14:15-35, Psalm 44:13-26"],
        103: [False, "Deuteronomy 19, Deuteronomy 20, Luke 15:1-32, Psalm 45:1-9"],
        104: [False, "Deuteronomy 21, Deuteronomy 22, Luke 16:1-18, Proverbs 9:13-18"],
        105: [False, "Deuteronomy 23, Deuteronomy 24, Deuteronomy 25:1-19, Luke 16:19-31, Luke 17:1-10, Psalm 45:10-17"],
        106: [False, "Deuteronomy 26, Deuteronomy 27, Deuteronomy 28:1-14, Luke 17:11-37, Psalm 46:1-11"],
        107: [False, "Deuteronomy 28:15-68, Luke 18:1-30, Psalm 47:1-9"],
        108: [False, "Deuteronomy 29, Deuteronomy 30:1-10, Luke 18:31-43, Luke 19:1-10, Proverbs 10:1-10"],
        109: [False, "Deuteronomy 30:11-20, Deuteronomy 31:1-29, Luke 19:11-44, Psalm 48:1-8"],
        110: [False, "Deuteronomy 31:30, Deuteronomy 32, Luke 19:45-48, Luke 20:1-26, Psalm 48:9-14"],
        111: [False, "Deuteronomy 33, Deuteronomy 34:1-12, Luke 20:27-47, Luke 21:1-4, Psalm 49:1-20"],
        112: [False, "Joshua 1, Joshua 2, Luke 21:5-38, Proverbs 10:11-20"],
        113: [False, "Joshua 3, Joshua 4, Joshua 5:1-12, Luke 22:1-38, Psalm 50:1-15"],
        114: [False, "Joshua 5:13-15, Joshua 6, Joshua 7, Luke 22:39-62, Psalm 50:16-23"],
        115: [False, "Joshua 8, Joshua 9:1-15, Luke 22:63-71, Luke 23:1-25, Psalm 51:1-9"],
        116: [False, "Joshua 9:16-27, Joshua 10, Luke 23:26-56, Proverbs 10:21-30"],
        117: [False, "Joshua 11, Joshua 12, Luke 24:1-35, Psalm 51:10-19"],
        118: [False, "Joshua 13, Joshua 14, Luke 24:36-53, Psalm 52:1-9"],
        119: [False, "Joshua 15, Joshua 16, John 1:1-28, Psalm 53:1-6"],
        120: [False, "Joshua 17, Joshua 18, John 1:29-51, Proverbs 10:31-32, Proverbs 11:1-8"],
        121: [False, "Joshua 19, Joshua 20, Joshua 21:1-19, John 2:1-25, Psalm 54:1-7"],
        122: [False, "Joshua 21:20-45, Joshua 22, John 3:1-21, Psalm 55:1-11"],
        123: [False, "Joshua 23, Joshua 24, John 3:22-36, Psalm 55:12-23"],
        124: [False, "Judges 1, Judges 2:1-5, John 4:1-26, Proverbs 11:9-18"],
        125: [False, "Judges 2:6-23, Judges 3, John 4:27-42, Psalm 56:1-13"],
        126: [False, "Judges 4, Judges 5, John 4:43-54, John 5:1-15, Psalm 57:1-6"],
        127: [False, "Judges 6, Judges 7:1-8, John 5:16-30, Psalm 57:7-11"],
        128: [False, "Judges 7:8-25, Judges 8, John 5:31-47, Proverbs 11:19-28"],
        129: [False, "Judges 9, John 6:1-24, Psalm 58:1-11"],
        130: [False, "Judges 10, Judges 11, John 6:25-59, Psalm 59:1-8"],
        131: [False, "Judges 12, Judges 13, John 6:60-71, John 7:1-13, Psalm 59:9-19"],
        132: [False, "Judges 14, Judges 15, John 7:14-44, Proverbs 11:29-31, Proverbs 12:1-7"],
        133: [False, "Judges 16, Judges 17, John 7:45-53, John 8:1-11, Psalm 60:1-4"],
        134: [False, "Judges 18, Judges 19, John 8:12-30, Psalm 60:5-12"],
        135: [False, "Judges 20, Judges 21, John 8:31-59, Psalm 61:1-8"],
        136: [False, "Ruth 1, Ruth 2, John 9:1-34, Proverbs 12:8-17"],
        137: [False, "Ruth 3, Ruth 4, John 9:35-41, John 10:1-21, Psalm 62:1-12"],
        138: [False, "1 Samuel 1, 1 Samuel 2:1-26, John 10:22-42, Psalm 63:1-11"],
        139: [False, "1 Samuel 2:27-36, 1 Samuel 3, 1 Samuel 4, John 11:1-44, Psalm 64:1-10"],
        140: [False, "1 Samuel 5, 1 Samuel 6, 1 Samuel 7, John 11:45-57, John 12:1-11, Proverbs 12:18-27"],
        141: [False, "1 Samuel 8, 1 Samuel 9, 1 Samuel 10:1-8, John 12:12-26, Psalm 65:1-13"],
        142: [False, "1 Samuel 10:9-27, 1 Samuel 11, 1 Samuel 12, John 12:37-50, John 13:1-17, Psalm 66:1-12"],
        143: [False, "1 Samuel 13, 1 Samuel 14:1-23, John 13:18-38, Psalm 66:13-20"],
        144: [False, "1 Samuel 14:24-52, 1 Samuel 15, John 14:1-31, Proverbs 12:28, Proverbs 13:1-9"],
        145: [False, "1 Samuel 16, 1 Samuel 17:1-37, John 15, John 16:1-4, Psalm 67:1-7"],
        146: [False, "1 Samuel 17:38-58, 1 Samuel 18, John 16:5-33, John 17:1-5, Psalm 68:1-6"],
        147: [False, "1 Samuel 19, 1 Samuel 20, John 17:6-26, Psalm 68:7-14"],
        148: [False, "1 Samuel 21, 1 Samuel 22, 1 Samuel 23, John 18:1-24, Proverbs 13:10-19"],
        149: [False, "1 Samuel 24, 1 Samuel 25, John 18:25-40, Psalm 68:15-20"],
        150: [False, "1 Samuel 26, 1 Samuel 27, 1 Samuel 28, John 19:1-27, Psalm 68:21-27"],
        151: [False, "1 Samuel 29, 1 Samuel 30, 1 Samuel 31, John 19:28-42, John 20:1-9, Psalm 68:28-35"],
        152: [False, "2 Samuel 1, 2 Samuel 2:1-7, John 20:10-31, Proverbs 13:20-25, Proverbs 14:1-4"],
        153: [False, "2 Samuel 2:8-32, 2 Samuel 3:1-21, John 21:1-25, Psalm 69:1-12"],
        154: [False, "2 Samuel 3:22-39, 2 Samuel 4, 2 Samuel 5:1-5, Acts 1:1-22, Psalm 69:13-28"],
        155: [False, "2 Samuel 5:6-25, 2 Samuel 6, Acts 1:23-26, Acts 2:1-21, Psalm 69:29-36"],
        156: [False, "2 Samuel 7, 2 Samuel 8, Acts 2:22-47, Proverbs 14:4-14"],
        157: [False, "2 Samuel 9, 2 Samuel 10, Acts 3, Psalm 70:1-5"],
        158: [False, "2 Samuel 11, 2 Samuel 12, Acts 4:1-22, Psalm 71:1-8"],
        159: [False, "2 Samuel 13, Acts 4:23-37, Acts 5:1-11, Psalm 71:9-18"],
        160: [False, "2 Samuel 14, 2 Samuel 15:1-12, Acts 5:12-42, Proverbs 14:15-24"],
        161: [False, "2 Samuel 15:13-37, 2 Samuel 16:1-14, Acts 6, Acts 7:1-19, Psalm 71:19-24"],
        162: [False, "2 Samuel 16:15-23, 2 Samuel 17, 2 Samuel 18:1-18, Acts 7:20-43, Psalm 72:1-20"],
        163: [False, "2 Samuel 18:19-33, 2 Samuel 19, Acts 7:44-60, Acts 8:1-3, Psalm 73:1-14"],
        164: [False, "2 Samuel 20, 2 Samuel 21, Acts 8:4-40, Proverbs 14:25-35"],
        165: [False, "2 Samuel 22, 2 Samuel 23:1-7, Acts 9:1-31, Psalm 73:15-28"],
        166: [False, "2 Samuel 23:8-39, 2 Samuel 24:1-25, Acts 9:32-43, Acts 10:1-23, Psalms 74:1-9"],
        167: [False, "1 Kings 1, 1 Kings 2:1-12, Acts 10:23-48, Acts 11:1-18, Psalm 74:10-17"],
        168: [False, "1 Kings 2:13-46, 1 Kings 3:1-15, Acts 11:19-30, Acts 12:1-19, Proverbs 15:1-10"],
        169: [False, "1 Kings 3:16-28, 1 Kings 4, 1 Kings 5, Acts 12:19-25, Acts 13:1-12, Psalm 74:18-23"],
        170: [False, "1 Kings 6, 1 Kings 7:1-22, Acts 13:13-41, Psalm 75:1-10"],
        171: [False, "1 Kings 7:23-51, 1 Kings 8:1-21, Acts 13:42-52, Acts 14:1-7, Psalm 76:1-12"],
        172: [False, "1 Kings 8:22-66, 1 Kings 9:1-9, Acts 14:8-28, Proverbs 15:11-20"],
        173: [False, "1 Kings 9:10-28, 1 Kings 10, 1 Kings 11:1-13, Acts 15:1-21, Psalm 77:1-9"],
        174: [False, "1 Kings 11:14-43, 1 Kings 12:1-24, Acts 15:22-41, Psalm 77:10-20"],
        175: [False, "1 Kings 12:25-33, 1 Kings 13, 1 Kings 14:1-20, Acts 16:1-15, Psalm 78:1-8"],
        176: [False, "1 Kings 14:21-31, 1 Kings 15, 1 Kings 16:1-7, Acts 16:16-40, Proverbs 15:21-30"],
        177: [False, "1 Kings 16:8-34, 1 Kings 17, 1 Kings 18:1-15, Acts 17:1-21, Psalm 78:9-16"],
        178: [False, "1 Kings 18:16-46, 1 Kings 19, Acts 17:22-34, Acts 18:1-8, Psalm 78:17-31"],
        179: [False, "1 Kings 20, 1 Kings 21, Acts 18:9-28, Acts 19:1-13, Psalm 78:32-39"],
        180: [False, "1 Kings 22:1-53, Acts 19:14-41, Proverbs 15:31-33, Proverbs 16:1-7"],
        181: [False, "2 Kings 1, 2 Kings 2:1-25, Acts 20:1-38, Psalm 78:40-55"],
        182: [False, "2 Kings 3, 2 Kings 4:1-37, Acts 21:1-26, Psalm 78:56-72"],
        183: [False, "2 Kings 4:38-44, 2 Kings 5, 2 Kings 6:1-23, Acts 21:27-40, Acts 22:1-22, Psalm 79:1-13"],
        184: [False, "2 Kings 6:24-33, 2 Kings 7, 2 Kings 8:1-15, Acts 22:22-30, Acts 23:1-11, Proverbs 16:8-17"],
        185: [False, "2 Kings 8:16-29, 2 Kings 9, Acts 23:12-35, Psalm 80:1-7"],
        186: [False, "2 Kings 10, 2 Kings 11, Acts 24:1-27, Psalm 80:8-19"],
        187: [False, "2 Kings 12, 2 Kings 13, 2 Kings 14:1-22, Acts 25:1-22, Psalm 81:1-7"],
        188: [False, "2 Kings 14:23-29, 2 Kings 15, Acts 25:23-27, Acts 26:1-23, Proverbs 16:18-27"],
        189: [False, "2 Kings 16, 2 Kings 17, Acts 26:24-32, Acts 27:1-12, Psalm 81:8-16"],
        190: [False, "2 Kings 18, 2 Kings 19:1-13, Acts 27:13-44, Psalm 82:1-8"],
        191: [False, "2 Kings 19:14-37, 2 Kings 20, Acts 28:1-16, Psalm 83:1-18"],
        192: [False, "2 Kings 21, 2 Kings 22, Acts 28:17-31, Proverbs 16:28-33, Proverbs 17:1-4"],
        193: [False, "2 Kings 23, 2 Kings 24:1-7, Romans 1:1-17, Psalm 84:1-7"],
        194: [False, "2 Kings 24:8-20, 2 Kings 25, Romans 1:18-32, Psalm 84:8-12"],
        195: [False, "Jonah 1, Jonah 2, Jonah 3, Jonah 4, Romans 2:1-16, Psalm 85:1-7"],
        196: [False, "Amos 1, Amos 2, Romans 2:17-29, Romans 3:1-8, Proverbs 17:5-14"],
        197: [False, "Amos 3, Amos 4, Romans 3:9-31, Psalm 85:8-13"],
        198: [False, "Amos 5, Romans 4:1-15, Psalm 86:1-10"],
        199: [False, "Amos 6, Amos 7, Romans 4:16-25, Romans 5:1-11, Psalm 86:11-17"],
        200: [False, "Amos 8, Amos 9, Romans 5:12-21, Proverbs 17:15-24"],
        201: [False, "Hosea 1, Hosea 2, Romans 6:1-14, Psalm 87:1-7"],
        202: [False, "Hosea 3, Hosea 4, Hosea 5, Romans 6:15-23, Romans 7:1-6, Psalm 88:1-9"],
        203: [False, "Hosea 6, Hosea 7, Romans 7:7-25, Psalm 88:9-18"],
        204: [False, "Hosea 8, Hosea 9, Romans 8:1-17, Proverbs 17:25-28, Proverbs 18:1-6"],
        205: [False, "Hosea 10, Hosea 11, Romans 8:18-39, Psalm 89:1-8"],
        206: [False, "Hosea 11, Hosea 12, Hosea 13, Hosea 14, Romans 9:1-21, Psalm 89:9-13"],
        207: [False, "1 Chronicles 1, 1 Chronicles 2:1-17, Romans 9:22-33, Romans 10:1-4, Psalm 89:14-18"],
        208: [False, "1 Chronicles 2:18-55, 1 Chronicles 3, 1 Chronicles 4:1-8, Romans 10:5-21, Romans 11:1-10, Proverbs 18:7-16"],
        209: [False, "1 Chronicles 4:9-43, 1 Chronicles 5, Romans 11:11-32, Psalm 89:19-29"],
        210: [False, "1 Chronicles 6, Romans 11:33-36, Romans 12:1-21, Psalm 89:30-37"],
        211: [False, "1 Chronicles 7, 1 Chronicles 8, Romans 13:1-14, Psalm 89:38-45"],
        212: [False, "1 Chronicles 9, 1 Chronicles 10:1-14, Romans 14:1-18, Proverbs 18:17-24, Proverbs 19:1-2"],
        213: [False, "1 Chronicles 11, 1 Chronicles 12:1-22, Romans 14:19-23, Romans 15:1-13, Psalm 89:46-52"],
        214: [False, "1 Chronicles 12:23-40, 1 Chronicles 13, 1 Chronicles 14, Romans 15:14-33, Psalm 90:1-10"],
        215: [False, "1 Chronicles 15, 1 Chronicles 16:1-36, Romans 16, Psalm 90:11-17"],
        216: [False, "1 Chronicles 16:37-43, 1 Chronicles 17, 1 Chronicles 18, 1 Corinthians 1:1-17, Proverbs 19:3-12"],
        217: [False, "1 Chronicles 19, 1 Chronicles 20, 1 Chronicles 21, 1 Corinthians 1:18-31, 1 Corinthians 2:1-5, Psalm 91:1-8"],
        218: [False, "1 Chronicles 22, 1 Chronicles 23, 1 Corinthians 2:6-16, Psalm 91:9-16"],
        219: [False, "1 Chronicles 24, 1 Chronicles 25, 1 Chronicles 26:1-19, 1 Corinthians 3, Psalm 92:1-15"],
        220: [False, "1 Chronicles 26:20-32, 1 Chronicles 27, 1 Corinthians 4, Proverbs 19:13-22"],
        221: [False, "1 Chronicles 28, 1 Chronicles 29, 1 Corinthians 5, Psalm 93:1-5"],
        222: [False, "2 Chronicles 1:1-17, 1 Corinthians 6, Psalm 94:1-11"],
        223: [False, "Ecclesiastes 1, Ecclesiastes 2, Ecclesiastes 3:1-22, 1 Corinthians 7:1-16, Psalm 94:12-23"],
        224: [False, "Ecclesiastes 4, Ecclesiastes 5, Ecclesiastes 6, 1 Corinthians 7:17-35, Proverbs 19:23-29, Proverbs 20:1-4"],
        225: [False, "Ecclesiastes 7, Ecclesiastes 8, Ecclesiastes 9:1-12, 1 Corinthians 7:36-40, 1 Corinthians 8:1-13, Psalm 95:1-11"],
        226: [False, "Ecclesiastes 9:13-18, Ecclesiastes 10, Ecclesiastes 11, Ecclesiastes 12, 1 Corinthians 9:1-18, Psalm 96:1-13"],
        227: [False, "2 Chronicles 2, 2 Chronicles 3, 2 Chronicles 4, 2 Chronicles 5:1, 1 Corinthians 9:19-27, 1 Corinthians 10:1-13, Psalm 97:1-12"],
        228: [False, "2 Chronicles 5:2-14, 2 Chronicles 6, 2 Chronicles 7:1-10, 1 Corinthians 10:14-33, 1 Corinthians 11:1, Proverbs 20:5-14"],
        229: [False, "2 Chronicles 7:11-22, 2 Chronicles 8, 2 Chronicles 9, 1 Corinthians 11:2-34, Psalm 98:1-9"],
        230: [False, "Song 1, Song 2, Song 3, Song 4, 1 Corinthians 12:1-26, Psalm 99:1-9"],
        231: [False, "Song 5, Song 6, Song 7, Song 8, 1 Corinthians 12:27-31, 1 Corinthians 13:1-13, Psalm 100:1-5"],
        232: [False, "2 Chronicles 10, 2 Chronicles 11, 2 Chronicles 12, 1 Corinthians 14:1-19, Proverbs 20:15-24"],
        233: [False, "2 Chronicles 13, 2 Chronicles 14, 2 Chronicles 15, 1 Corinthians 14:20-40, Psalm 101:1-8"],
        234: [False, "2 Chronicles 16, 2 Chronicles 17, 2 Chronicles 18:1-27, 1 Corinthians 15:1-34, Psalm 102:1-11"],
        235: [False, "2 Chronicles 18:28-34, 2 Chronicles 19, 2 Chronicles 20, 1 Corinthians 15:35-49, Psalm 102:12-17"],
        236: [False, "2 Chronicles 21, 2 Chronicles 22, 2 Chronicles 23, 1 Corinthians 15:50-58, 1 Corinthians 16:1-4, Proverbs 20:25-30, Proverbs 21:1-4"],
        237: [False, "2 Chronicles 24, 2 Chronicles 25, 1 Corinthians 16:5-24, Psalm 102:18-28"],
        238: [False, "2 Chronicles 26, 2 Chronicles 27, 2 Chronicles 28, 2 Corinthians 1:1-11, Psalm 103:1-12"],
        239: [False, "2 Chronicles 29, 2 Chronicles 30, 2 Chronicles 31:1, 2 Corinthians 1:12-22, Psalm 103:13-22"],
        240: [False, "2 Chronicles 31:2-21, 2 Chronicles 32, 2 Chronicles 33:1-20, 2 Corinthians 1:23, 2 Corinthians 2:1-11, Proverbs 21:5-16"],
        241: [False, "2 Chronicles 33:21-24, 2 Chronicles 34, 2 Chronicles 35:1-19, 2 Corinthians 2:12-17, 2 Corinthians 3:1-6, Psalm 104:1-18"],
        242: [False, "2 Chronicles 35:20-27, 2 Chronicles 36, 2 Corinthians 3:7-18, Psalm 104:19-30"],
        243: [False, "Micah 1, Micah 2, Micah 3, Micah 4, 2 Corinthians 4, Psalm 104:31-35"],
        244: [False, "Micah 5, Micah 6, Micah 7, 2 Corinthians 5:1-10, Proverbs 21:17-26"],
        245: [False, "Isaiah 1, Isaiah 2, 2 Corinthians 5:11-21, 2 Corinthians 6:1-2, Psalm 105:1-11"],
        246: [False, "Isaiah 3, Isaiah 4, Isaiah 5:1-7, 2 Corinthians 6:3-18, 2 Corinthians 7:1, Psalm 105:12-22"],
        247: [False, "Isaiah 5:8-30, Isaiah 6, Isaiah 7, Isaiah 8:1-10, 2 Corinthians 7:2-16, Psalm 105:23-36"],
        248: [False, "Isaiah 8:11-22, Isaiah 9, Isaiah 10:1-19, 2 Corinthians 8:1-15, Proverbs 21:27-31, Proverbs 22:1-6"],
        249: [False, "Isaiah 10:20-34, Isaiah 11, Isaiah 12, Isaiah 13, 2 Corinthians 8:16-24, 2 Corinthians 9:1-5, Psalm 105:37-45"],
        250: [False, "Isaiah 14, Isaiah 15, Isaiah 16, 2 Corinthians 9:6-15, Psalm 106:1-15"],
        251: [False, "Isaiah 17, Isaiah 18, Isaiah 19, 2 Corinthians 10, Psalm 106:16-31"],
        252: [False, "Isaiah 20, Isaiah 21, Isaiah 22, Isaiah 23, 2 Corinthians 11:1-15, Proverbs 22:7-16"],
        253: [False, "Isaiah 24, Isaiah 25, Isaiah 26, 2 Corinthians 11:16-33, Psalm 106:32-39"],
        254: [False, "Isaiah 27, Isaiah 28, 2 Corinthians 12:1-10, Psalm 106:40-48"],
        255: [False, "Isaiah 29, Isaiah 30:1-18, 2 Corinthians 12:11-21, Psalm 107:1-9"],
        256: [False, "Isaiah 30:19-33, Isaiah 31, Isaiah 32, 2 Corinthians 13, Proverbs 22:17-27"],
        257: [False, "Isaiah 33, Isaiah 34, Isaiah 35, Galatians 1, Psalm 107:10-22"],
        258: [False, "Isaiah 36, Isaiah 37, Galatians 2:1-10, Psalm 107:23-32"],
        259: [False, "Isaiah 38, Isaiah 39, Isaiah 40, Galatians 2:11-21, Galatians 3:1-9, Psalm 107:33-43"],
        260: [False, "Isaiah 41, Isaiah 42, Galatians 3:10-25, Proverbs 22:28-29, Proverbs 23:1-9"],
        261: [False, "Isaiah 43, Isaiah 44:1-23, Galatians 3:26-29, Galatians 4:1-20, Psalm 108:1-5"],
        262: [False, "Isaiah 44:24-28, Isaiah 45, Isaiah 46, Galatians 4:21-31, Galatians 5:1-6, Psalm 108:6-13"],
        263: [False, "Isaiah 47, Isaiah 48, Isaiah 49:1-7, Galatians 5:7-26, Psalm 109:1-20"],
        264: [False, "Isaiah 49:8-26, Isaiah 50, Isaiah 51:1-16, Galatians 6, Proverbs 23:10-18"],
        265: [False, "Isaiah 51:17-23, Isaiah 52, Isaiah 53, Isaiah 54, Ephesians 1, Psalm 109:21-31"],
        266: [False, "Isaiah 55, Isaiah 56, Isaiah 57:1-13, Ephesians 2, Psalm 110:1-7"],
        267: [False, "Isaiah 57:14-21, Isaiah 58, Isaiah 59, Ephesians 3, Psalm 111:1-10"],
        268: [False, "Isaiah 60, Isaiah 61, Isaiah 62, Ephesians 4:1-16, Proverbs 23:19-28"],
        269: [False, "Isaiah 63, Isaiah 64, Isaiah 65:1-16, Ephesians 4:17-32, Ephesians 5:1-7, Psalm 112:1-10"],
        270: [False, "Isaiah 65:17-25, Isaiah 66, Ephesians 5:8-33, Psalm 113:1-9"],
        271: [False, "Nahum 1, Nahum 2, Nahum 3, Ephesians 6, Psalm 114:1-8"],
        272: [False, "Zephaniah 1, Zephaniah 2, Zephaniah 3, Philippians 1:1-26, Proverbs 23:29-35, Proverbs 24:1-4"],
        273: [False, "Jeremiah 1, Jeremiah 2:1-30, Philippians 1:27-30, Philippians 2:1-11, Psalm 115:1-11"],
        274: [False, "Jeremiah 2:31-47, Jeremiah 3, Jeremiah 4:1-9, Philippians 2:12-30, Psalm 115:12-18"],
        275: [False, "Jeremiah 4:10-31, Jeremiah 5, Philippians 3, Philippians 4:1, Psalm 116:1-11"],
        276: [False, "Jeremiah 6, Jeremiah 7:1-29, Philippians 4:2-23, Proverbs 24:5-14"],
        277: [False, "Jeremiah 7:30-34, Jeremiah 8, Jeremiah 9:1-16, Colossians 1:1-23, Psalm 116:12-19"],
        278: [False, "Jeremiah 9:17-26, Jeremiah 10, Jeremiah 11:1-17, Colossians 1:24-29, Colossians 2:1-5, Psalm 117:1-2"],
        279: [False, "Jeremiah 11:18-23, Jeremiah 12, Jeremiah 13, Colossians 2:6-23, Psalm 118:1-16"],
        280: [False, "Jeremiah 14, Jeremiah 15, Colossians 3, Colossians 4:1, Proverbs 24:15-22"],
        281: [False, "Jeremiah 16, Jeremiah 17, Colossians 4:2-18, Psalm 118:17-29"],
        282: [False, "Jeremiah 18, Jeremiah 19, Jeremiah 20, 1 Thessalonians 1, 1 Thessalonians 2:1-16, Psalm 119:1-8"],
        283: [False, "Jeremiah 21, Jeremiah 22, Jeremiah 23:1-8, 1 Thessalonians 2:17-19, 1 Thessalonians 3, Psalm 119:9-16"],
        284: [False, "Jeremiah 23:9-40, Jeremiah 24, Jeremiah 25:1-14, 1 Thessalonians 4, Proverbs 24:23-34"],
        285: [False, "Jeremiah 25:15-38, Jeremiah 26, 1 Thessalonians 5, Psalm 119:17-24"],
        286: [False, "Jeremiah 27, Jeremiah 28, Jeremiah 29:1-23, 2 Thessalonians 1, Psalm 119:25-32"],
        287: [False, "Jeremiah 29:24-32, Jeremiah 30, Jeremiah 31:1-14, 2 Thessalonians 2, Psalm 119:33-40"],
        288: [False, "Jeremiah 31:15-40, Jeremiah 32:1-25, 2 Thessalonians 3, Proverbs 25:1-10"],
        289: [False, "Jeremiah 32:26-44, Jeremiah 33, Jeremiah 34, 1 Timothy 1, Psalm 119:41-48"],
        290: [False, "Jeremiah 35, Jeremiah 36, Jeremiah 37, 1 Timothy 2, Psalm 119:49-56"],
        291: [False, "Jeremiah 38, Jeremiah 39, Jeremiah 40:1-6, 1 Timothy 3, Psalm 119:57-64"],
        292: [False, "Jeremiah 40:7-16, Jeremiah 41, Jeremiah 42, 1 Timothy 4, Proverbs 25:11-20"],
        293: [False, "Jeremiah 43, Jeremiah 44, Jeremiah 45, 1 Timothy 5, 1 Timothy 6:1-2, Psalm 119:65-72"],
        294: [False, "Jeremiah 46, Jeremiah 47, 1 Timothy 6:3-21, Psalm 119:73-80"],
        295: [False, "Jeremiah 48, Jeremiah 49:1-6, 2 Timothy 1, Psalm 119:81-88"],
        296: [False, "Jeremiah 49:7-39, Jeremiah 50:1-10, 2 Timothy 2, Proverbs 25:21-28, Proverbs 26:1-2"],
        297: [False, "Jeremiah 50:11-46, Jeremiah 51:1-14, 2 Timothy 3, Psalm 119:89-96"],
        298: [False, "Jeremiah 51:15-64, 2 Timothy 4, Psalm 119:97-104"],
        299: [False, "Jeremiah 52, Titus 1, Psalm 119:105-112"],
        300: [False, "Habakkuk 1, Habakkuk 2, Habakkuk 3:1-19, Titus 2, Proverbs 26:3-12"],
        301: [False, "Lamentations 1, Lamentations 2:1-6, Titus 3, Psalm 119:113-120"],
        302: [False, "Lamentations 2:7-27, Lamentations 3:1-39, Philemon 1, Psalm 119:121-128"],
        303: [False, "Lamentations 3:40-66, Lamentations 4, Lamentations 5, Hebrews 1, Psalm 119:129-136"],
        304: [False, "Obadiah 1, Hebrews 2, Proverbs 26:13-22"],
        305: [False, "Joel 1, Joel 2:1-17, Hebrews 3, Psalm 119:137-144"],
        306: [False, "Joel 2:18-32, Joel 3, Hebrews 4:1-13, Psalm 119:145-152"],
        307: [False, "Ezekiel 1, Ezekiel 2, Ezekiel 3, Hebrews 4:14-16, Hebrews 5:1-10, Psalm 119:153-160"],
        308: [False, "Ezekiel 4, Ezekiel 5, Ezekiel 6, Hebrews 5:11-14, Hebrews 6:1-12, Proverbs 26:23-28, Proverbs 27:1-4"],
        309: [False, "Ezekiel 7, Ezekiel 8, Ezekiel 9, Hebrews 6:13-20, Hebrews 7:1-10, Psalm 119:161-168"],
        310: [False, "Ezekiel 10, Ezekiel 11, Ezekiel 12, Hebrews 7:11-28, Psalm 119:169-176"],
        311: [False, "Ezekiel 13, Ezekiel 14, Ezekiel 15, Hebrews 8, Psalm 120:1-7"],
        312: [False, "Ezekiel 16, Hebrews 9:1-15, Proverbs 27:5-14"],
        313: [False, "Ezekiel 17, Ezekiel 18, Hebrews 9:16-28, Psalm 121:1-8"],
        314: [False, "Ezekiel 19, Ezekiel 20:1-44, Hebrews 10:1-18, Psalm 122:1-9"],
        315: [False, "Ezekiel 20:45-49, Ezekiel 21, Ezekiel 22:1-22, Hebrews 10:19-39, Psalm 123:1-4"],
        316: [False, "Ezekiel 22:23-31, Ezekiel 23, Hebrews 11:1-16, Proverbs 27:15-22"],
        317: [False, "Ezekiel 24, Ezekiel 25, Hebrews 11:17-40, Psalm 124:1-8"],
        318: [False, "Ezekiel 26, Ezekiel 27, Hebrews 12:1-13, Psalm 125:1-5"],
        319: [False, "Ezekiel 28, Ezekiel 29, Hebrews 12:14-29, Psalm 126:1-6"],
        320: [False, "Ezekiel 30, Ezekiel 31, Hebrews 13, Proverbs 27:23-27, Proverbs 28:1-6"],
        321: [False, "Ezekiel 32, Ezekiel 33:1-32, James 1, Psalm 127:1-5"],
        322: [False, "Ezekiel 33:21-33, Ezekiel 34, Ezekiel 35, James 2, Psalm 128:1-6"],
        323: [False, "Ezekiel 36, Ezekiel 37, James 3, Psalm 129:1-8"],
        324: [False, "Ezekiel 38, Ezekiel 39, James 4, Proverbs 28:7-17"],
        325: [False, "Ezekiel 40, James 5, Psalm 130:1-8"],
        326: [False, "Ezekiel 41, Ezekiel 42, 1 Peter 1, 1 Peter 2:1-3, Psalm 131:1-3"],
        327: [False, "Ezekiel 43, Ezekiel 44, 1 Peter 2:4-25, Psalm 132:1-18"],
        328: [False, "Ezekiel 45, Ezekiel 46, 1 Peter 3, Proverbs 28:18-28"],
        329: [False, "Ezekiel 47, Ezekiel 48, 1 Peter 4, Psalm 133:1-3"],
        330: [False, "Daniel 1, Daniel 2:1-23, 1 Peter 5, Psalm 134:1-3"],
        331: [False, "Daniel 2:24-49, Daniel 3:1-12, 2 Peter 1, Psalm 135:1-12"],
        332: [False, "Daniel 3:13-30, Daniel 4:1-18, 2 Peter 2, Proverbs 29:1-9"],
        333: [False, "Daniel 4:19-37, Daniel 5:1-16, 2 Peter 3, Psalm 135:13-21"],
        334: [False, "Daniel 5:17-31, Daniel 6:1-28, 1 John 1, 1 John 2, Psalm 136:1-12"],
        335: [False, "Daniel 7, Daniel 8:1-14, 1 John 2:12-27, Psalm 136:13-26"],
        336: [False, "Daniel 8:15-27, Daniel 9:1-19, 1 John 2:28-29, 1 John 3:1-10, Proverbs 29:10-18"],
        337: [False, "Daniel 9:20-27, Daniel 10, Daniel 11:1, 1 John 3:11-24, 1 John 4:1-6, Psalm 137:1-9"],
        338: [False, "Daniel 11:2-35, 1 John 4:7-21, Psalm 138:1-8"],
        339: [False, "Daniel 11:36-45, Daniel 12, 1 John 5:1-21, Psalm 139:1-10"],
        340: [False, "Haggai 1, Haggai 2:1-23, 2 John 1:1-13, Proverbs 29:19-27"],
        341: [False, "Zechariah 1, Zechariah 2, Zechariah 3, Zechariah 4, 3 John 1:1-14, Psalm 139:11-16"],
        342: [False, "Zechariah 5, Zechariah 6, Zechariah 7, Zechariah 8, Jude 1:1-25, Psalm 139:17-24"],
        343: [False, "Zechariah 9, Zechariah 10, Zechariah 11, Revelation 1, Psalm 140:1-5"],
        344: [False, "Zechariah 12, Zechariah 13, Zechariah 14, Revelation 2:1-17, Proverbs 30:1-10"],
        345: [False, "Esther 1, Esther 2:1-18, Revelation 2:18-29, Revelation 3:1-6, Psalm 140:6-13"],
        346: [False, "Esther 2:19-23, Esther 3, Esther 4, Esther 5, Revelation 3:7-22, Psalm 141:1-10"],
        347: [False, "Esther 6, Esther 7, Esther 8, Revelation 4, Psalm 142:1-11"],
        348: [False, "Esther 9, Esther 10, Revelation 5, Proverbs 30:11-23"],
        349: [False, "Malachi 1, Malachi 2:1-16, Revelation 6, Psalm 143:1-12"],
        350: [False, "Malachi 2:17, Malachi 3, Malachi 4, Revelation 7, Psalm 144:1-8"],
        351: [False, "Ezra 1, Ezra 2:1-67, Revelation 8, Revelation 9:1-12, Psalm 144:9-15"],
        352: [False, "Ezra 2:68-70, Ezra 3, Ezra 4:1-5, Revelation 9:13-21, Revelation 10, Proverbs 30:24-33"],
        353: [False, "Ezra 4:6-24, Ezra 5, Revelation 11, Psalm 145:1-7"],
        354: [False, "Ezra 6, Ezra 7:1-10, Revelation 12, Revelation 13:1, Psalm 145:8-13"],
        355: [False, "Ezra 7:11-28, Ezra 8:1-14, Revelation 13:1-18, Psalm 145:13-21"],
        356: [False, "Ezra 8:15-36, Ezra 9:1-15, Revelation 14:1-13, Proverbs 31:1-9"],
        357: [False, "Ezra 10, Revelation 14:14-20, Revelation 15, Psalm 146:1-10"],
        358: [False, "Nehemiah 1, Nehemiah 2, Revelation 16, Psalm 147:1-11"],
        359: [False, "Nehemiah 3, Nehemiah 4, Revelation 17, Psalm 147:12-20"],
        360: [False, "Nehemiah 5, Nehemiah 6, Nehemiah 7:1-3, Revelation 18:1-17, Proverbs 31:10-20"],
        361: [False, "Nehemiah 7:4-73, Nehemiah 8, Revelation 18:17-24, Revelation 19:1-10, Psalm 148:1-6"],
        362: [False, "Nehemiah 9:1-37, Revelation 19:11-21, Psalm 148:7-14"],
        363: [False, "Nehemiah 9:38, Nehemiah 10, Nehemiah 11:1-21, Revelation 20, Psalm 149:1-9"],
        364: [False, "Nehemiah 11:22-36, Nehemiah 12:1-47, Revelation 21, Proverbs 31:21-31"],
        365: [False, "Nehemiah 13, Revelation 22, Psalm 150:1-6"],
    }

    translation = (
        "Bible Reading Plan",
        "Today is ",
        "Search: ",
        "Open in Tabs",
        "Hide Checked Items",
        "Show Checked Items",
        "Reset All Items",
        "Save Reading Progress",
        "Day ",
        "",
        "Your reading progress is saved in the following location:",
        "Failed to save your progress locally.  You may need to grant write permission to UBA.",
    )

    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        # set title
        self.setWindowTitle(self.translation[0])
        self.setMinimumSize(830, 500)
        # set variables
        self.setupVariables()
        # setup interface
        self.setupUI()

    def setupVariables(self):
        import copy, os
        from datetime import date
        self.today = date.today()
        self.todayNo = int(format(self.today, '%j'))
        if self.todayNo > 365:
            self.todayNo = 365
        self.progressFile = os.path.join(os.getcwd(), "plugins", "menu", "{0}.txt".format(self.translation[0]))
        if os.path.isfile(self.progressFile):
            from ast import literal_eval
            with open(self.progressFile, "r") as fileObj:
                self.plan = literal_eval(fileObj.read())
        else:
            self.plan = copy.deepcopy(self.template)
        self.hideCheckedItems = False

    def setupUI(self):
        from qtpy.QtGui import QStandardItemModel
        from qtpy.QtWidgets import (QPushButton, QLabel, QListView, QAbstractItemView, QHBoxLayout, QVBoxLayout, QLineEdit)

        mainLayout = QVBoxLayout()

        readingListLayout = QVBoxLayout()

        readingListLayout.addWidget(QLabel(self.translation[0]))
        readingListLayout.addWidget(QLabel("{0}{1}".format(self.translation[1], self.today)))

        filterLayout = QHBoxLayout()
        filterLayout.addWidget(QLabel(self.translation[2]))
        self.filterEntry = QLineEdit()
        self.filterEntry.textChanged.connect(self.resetItems)
        filterLayout.addWidget(self.filterEntry)
        readingListLayout.addLayout(filterLayout)

        self.readingList = QListView()
        self.readingList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.readingListModel = QStandardItemModel(self.readingList)
        self.readingList.setModel(self.readingListModel)
        self.resetItems()
        self.readingListModel.itemChanged.connect(self.itemChanged)
        #print(self.readingList.currentIndex().row())
        #self.readingList.selectionModel().selectionChanged.connect(self.function)
        readingListLayout.addWidget(self.readingList)

        buttonsLayout = QHBoxLayout()

        button = QPushButton(self.translation[3])
        button.clicked.connect(self.openInTabs)
        buttonsLayout.addWidget(button)

        self.hideShowButton = QPushButton(self.translation[4])
        self.hideShowButton.clicked.connect(self.hideShowCheckedItems)
        buttonsLayout.addWidget(self.hideShowButton)

        button = QPushButton(self.translation[6])
        button.clicked.connect(self.resetAllItems)
        buttonsLayout.addWidget(button)

        button = QPushButton(self.translation[7])
        button.clicked.connect(self.saveProgress)
        buttonsLayout.addWidget(button)

        mainLayout.addLayout(readingListLayout)
        mainLayout.addLayout(buttonsLayout)

        self.setLayout(mainLayout)

    def itemChanged(self, standardItem):
        from qtpy.QtCore import Qt
        key = int(standardItem.text().split(".")[0])
        if standardItem.checkState() is Qt.CheckState.Checked:
            self.plan[key][0] = True
        elif standardItem.checkState() is Qt.CheckState.Unchecked:
            self.plan[key][0] = False
        if self.hideCheckedItems:
            self.resetItems()

    def resetItems(self):
        from qtpy.QtGui import QStandardItem
        from qtpy.QtCore import Qt
        # Empty the model before reset
        self.readingListModel.clear()
        # Reset
        index = 0
        todayIndex = None
        filterEntry = self.filterEntry.text()
        for key, value in self.plan.items():
            checked, passages = value
            if not (self.hideCheckedItems and checked) and (filterEntry == "" or (filterEntry != "" and filterEntry.lower() in passages.lower())):
                item = QStandardItem("{0}. {1}".format(key, passages))
                item.setToolTip("{0}{1}{2}".format(self.translation[8], key, self.translation[9]))
                if key == self.todayNo:
                    todayIndex = index
                item.setCheckable(True)
                item.setCheckState(Qt.CheckState.Checked if checked else Qt.CheckState.Unchecked)
                self.readingListModel.appendRow(item)
                index += 1
        if todayIndex is not None:
            self.readingList.setCurrentIndex(self.readingListModel.index(todayIndex, 0))

    def hideShowCheckedItems(self):
        self.hideCheckedItems = not self.hideCheckedItems
        self.resetItems()
        self.hideShowButton.setText(self.translation[5] if self.hideCheckedItems else self.translation[4])

    def resetAllItems(self):
        import copy
        self.plan = copy.deepcopy(self.template)
        self.resetItems()

    def translateIntoChinese(self):
        import copy, pprint
        from util.BibleBooks import BibleBooks
        plan = copy.deepcopy(self.template)
        filePath = "{0}_zh".format(self.progressFile)
        with open(filePath, "w", encoding="utf-8") as fileObj:
            fileObj.write(pprint.pformat(plan))
        with open(filePath, "r") as fileObj:
            text = fileObj.read()
        translateDict = {}
        bookNames = []
        for key, value in BibleBooks.eng.items():
            bookName = value[-1]
            bookNames.append(bookName)
            translateDict[bookName] = BibleBooks.sc[key][-1]
        bookNames = sorted(bookNames, key=len, reverse=True)
        #print(bookNames)
        for name in bookNames:
            text = text.replace(name, translateDict[name])
        text = text.replace("Psalm", "诗篇")
        with open(filePath, "w", encoding="utf-8") as fileObj:
            fileObj.write(text)

    def saveProgress(self):
        import pprint
        from qtpy.QtWidgets import QMessageBox
        try:
            with open(self.progressFile, "w", encoding="utf-8") as fileObj:
                fileObj.write(pprint.pformat(self.plan))
            message = "{0}\n'{1}'".format(self.translation[10], self.progressFile)
        except:
            message = self.translation[11]
        QMessageBox.information(self, self.translation[0], message)

    def openInTabs(self):
        dayNo = self.readingList.currentIndex().row() + 1
        todayReading = self.plan[dayNo][-1].split(", ")
        openBibleWindowContentOnNextTab = config.openBibleWindowContentOnNextTab
        config.openBibleWindowContentOnNextTab = True
        for reading in todayReading:
            command = "MAIN:::{0}".format(reading)
            self.parent.runTextCommand(command)
        config.openBibleWindowContentOnNextTab = openBibleWindowContentOnNextTab
        self.close()

config.mainWindow.bibleReadingPlan = BibleReadingPlan(config.mainWindow)
config.mainWindow.bibleReadingPlan.show()
