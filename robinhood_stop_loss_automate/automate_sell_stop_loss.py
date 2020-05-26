import robin_stocks as r

class AutomationActions():
    def __init__(self):
        self.current_positions = r.build_holdings()

    def __cancel_all_open_positions(self):
        r.cancel_all_stock_orders()

    def apply_stop_loss_to_all_positions(self, percentage, cancel_previous=True):
        if cancel_previous:
            self.__cancel_all_open_positions()

        for key in self.current_positions:
            quantity = int(float(self.current_positions[key]['quantity']))
            response = r.orders.order_sell_trailing_stop(key, quantity, percentage, 'percentage')
            print(response)


def main():
    AutomationActions().apply_stop_loss_to_all_positions(5, False)


if __name__ == "__main__":
    main()
