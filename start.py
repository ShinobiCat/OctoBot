#  This file is part of OctoBot (https://github.com/Drakkar-Software/OctoBot)
#  Copyright (c) 2023 Drakkar-Software, All rights reserved.
#
#  OctoBot is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  OctoBot is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public
#  License along with OctoBot. If not, see <https://www.gnu.org/licenses/>.
import sys
import os

# Add local OctoBot directories to PYTHONPATH
sys.path.append(os.path.join(os.path.dirname(__file__), 'OctoBot'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'Async-Channel'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'OctoBot-Backtesting'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'OctoBot-Commons'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'OctoBot-Services'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'OctoBot-Evaluators'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'OctoBot-Trading'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'OctoBot-Tentacles-Manager'))

from octobot.cli import main

if __name__ == '__main__':
    main(sys.argv[1:])
