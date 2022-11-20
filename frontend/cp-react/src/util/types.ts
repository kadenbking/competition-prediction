export type OptionType = { label: string, value: number } | null;
export type OptionsType = Array<OptionType>;

export type Outcome = {
    winningTeam: string;
    losingTeam: string;
    percentage: string;
} | null;